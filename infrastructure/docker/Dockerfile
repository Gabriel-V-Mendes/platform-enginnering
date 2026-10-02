FROM node:22-bookworm-slim AS build
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 make g++ && \
    rm -rf /var/lib/apt/lists/*


COPY .yarn ./.yarn
COPY .yarnrc.yml ./
COPY backstage.json ./
COPY package.json yarn.lock ./
COPY packages packages/
COPY plugins plugins/

# Instala dependências
RUN yarn install --immutable

# Copia o restante do projeto e faz o build
COPY . .
RUN yarn tsc && yarn build:backend


FROM node:22-bookworm-slim
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip python3-venv curl && \
    rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --no-cache-dir mkdocs-techdocs-core

# Criação de usuário non-root 
RUN addgroup --system --gid 1001 backstage && \
    adduser --system --uid 1001 --gid 1001 backstage

# Copia arquivos necessários 
COPY --from=build --chown=backstage:backstage /app/.yarn ./.yarn
COPY --from=build --chown=backstage:backstage /app/.yarnrc.yml ./
COPY --from=build --chown=backstage:backstage /app/backstage.json ./

# Variável de produção
ENV NODE_ENV=production

# Copia skeleton do backend e instala apenas deps de produção
COPY --from=build --chown=backstage:backstage /app/yarn.lock /app/package.json ./
COPY --from=build --chown=backstage:backstage /app/packages/backend/dist/skeleton.tar.gz ./
RUN tar xzf skeleton.tar.gz && rm skeleton.tar.gz

RUN yarn workspaces focus --all --production && rm -rf "$(yarn cache clean)" 2>/dev/null || true

# Copia examples (necessário para os templates de exemplo do catálogo)
COPY --from=build --chown=backstage:backstage /app/examples ./examples

# Copia bundle do backend e configurações
COPY --from=build --chown=backstage:backstage /app/packages/backend/dist/bundle.tar.gz ./
RUN tar xzf bundle.tar.gz && rm bundle.tar.gz
COPY --from=build --chown=backstage:backstage /app/app-config*.yaml ./

# Copia TechDocs, templates e catalog-info para o container
COPY --from=build --chown=backstage:backstage /app/docs ./docs
COPY --from=build --chown=backstage:backstage /app/mkdocs.yml ./
COPY --from=build --chown=backstage:backstage /app/templates ./templates
COPY --from=build --chown=backstage:backstage /app/catalog-info.yaml ./

# Ajusta as permissões da pasta /app (apenas do diretório raiz) para evitar bloqueio
RUN chown backstage:backstage /app && chmod 755 /app

# Troca para o usuário seguro antes de executar a aplicação
USER backstage

EXPOSE 7007
CMD ["node", "packages/backend", "--config", "app-config.yaml", "--config", "app-config.production.yaml"]
