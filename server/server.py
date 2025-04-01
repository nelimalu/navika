from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get-data")
def get_data():
    with open('./data.json', 'r') as file:
        data = json.loads(file.read())
    print(data)
    return data


@app.get("/update/{request}")
def read_item(request):
    habit_id, weekday, index, new_value = request.split('-')

    try:
        with open('./data.json', 'r') as file:
            data = json.load(file)
            data[habit_id]['weekdays'][weekday][int(index)] = int(new_value)
        
        with open('./data.json', 'w') as file:
            json.dump(data, file, indent=4)

        return {'status': 'success'}
    except Exception as err:
        return {'status': f'error: {err}'}
