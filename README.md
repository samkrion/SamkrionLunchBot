# SamkrionLunchBot

Suggest meals near Samkrion, deploy on Lambda

# Build

- Work at project root

1. Build Docker builder image with `docker build -t lunchbot-builder .`
2. Generate Lambda Artifact ZIP with `docker run -it -v $(pwd):/mount lunchbot-builder bash /mount/build.sh`
3. Artifact ZIP will be generated with name `function.zip`.

# Deploy

1. Upload generated `function.zip` to Lambda.
2. Add following environment variables:
   | Name | Description |
   |-----------------|--------------------------------------------------------------------------------|
   | SLACK_URL | Slack Hook URL |
   | NOTION_TOKEN | Notion token_v2 (Check [Here](https://wh-y-j-lee.tistory.com/5) for more info) |
   | NOTION_DATA_DIR | `/tmp/notion-dir` |
