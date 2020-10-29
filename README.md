# SamkrionLunchBot

Suggest meals near Samkrion, deploy on Lambda

# HOW-TO

- Work at project root

1. Build Docker builder image with `docker build -t lunchbot-builder .`
2. Generate Lambda Artifact ZIP with `docker run -it -v $(pwd):/mount lunchbot-builder bash /mount/build.sh`
3. Artifact ZIP will be generated with name `function.zip`.
