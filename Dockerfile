FROM python:3

RUN pip install pip install git+https://github.com/vonloxley/obsidian-to-hugo.git@main

# Build:
# docker build -t o2h - < Dockerfile
#
# Run:
# docker run \
#     -u 1000:1000
#     -v /home/${USER}/zettelkasten:/tmp/in:ro \
#     -v /home/${USER}/websites/zettelkasten:/tmp/out \
#     --rm \
#     o2h \
#     python -m obsidian_to_hugo --obsidian-vault-dir=/tmp/in --hugo-content-dir=/tmp/out/content 
