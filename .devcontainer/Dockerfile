# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/devcontainers/typescript-node:20

# Stub for a future TeX Live layer. This allows us to add TeX tooling later
# without rebuilding the base image logic.
RUN mkdir -p /opt/texlive && \
    echo "TeX Live layer placeholder" > /opt/texlive/README

ENV PNPM_HOME=/usr/local/share/pnpm
ENV PATH="$PNPM_HOME:$PATH"

RUN corepack enable
