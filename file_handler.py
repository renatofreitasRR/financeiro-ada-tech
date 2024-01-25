import json

class FileHandler:

    def write_file(self, data):
        with open('data.json', 'w', encoding='utf-8') as f:

            content = {
                "data": data
            }

            json.dump(content, f, ensure_ascii=False)

    def get_file(self):

        try:
            file = open('data.json', 'r')
            content = file.read()
            file.close()

            if not content:
                return []
            else:
                data = json.loads(content)
                return data["data"]
        except FileNotFoundError:
            file = open('data.json', 'w')
            file.close()

            return []