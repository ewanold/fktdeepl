rem Test call to deepl via curl
curl -X POST https://api-free.deepl.com/v2/translate  -H "Authorization: DeepL-Auth-Key f5c84e42-f195-6b60-5f67-e13b97626693:fx"  -d "text=Hello, world!" -d "source_lang=EN"  -d "target_lang=RU"