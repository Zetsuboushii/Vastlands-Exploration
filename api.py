import datetime
import os
import shutil
import typing
from pathlib import Path
from typing import List, Dict, Any

import pandas as pd
import requests
from entities import Entity

API_URL = "https://tome.zetsuboushii.site/static/json/"


def get_data_by_api(key: str, endpoint: str, data_key: str = None) -> Dict[str, Any]:
    response = requests.get(endpoint)
    data = response.json()
    if data_key is not None:
        data = data.get(data_key, {})
    return data


def get_all_data() -> \
        Dict[str, Dict[str, Any]]:
    endpoints = {
        "characters_data": "characters.json",
        "current_data": "current_date.json",
        "gentarium_data": "gentarium.json",
        # "places_data": "places.json",
        # "actions_data": "actions.json",
        "bestiarium_data": "bestiarium.json",
        # "effect_data": "effects.json",
        # "weapons_data": "weapons.json",
        # "weapon_abilities_data": "abilities.json"
    }
    endpoints = {key: API_URL + endpoint for key, endpoint in endpoints.items()}
    data = {key: get_data_by_api(key, endpoint) for key, endpoint in
            endpoints.items()}
    return data


def get_df_from_endpoint_data(endpoint_data: List[Dict[str, Any]], type: typing.Type[Entity]):
    objects = [type.from_json(object_data) for object_data in endpoint_data]
    dicts = [object.__dict__ for object in objects]
    df = pd.DataFrame(dicts)
    return df


def fetch_faergria_map(faegria_map_url: str):
    data_dir = os.path.join(os.curdir, "data")
    map_location = os.path.join(data_dir, "faergria-map.png")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    if not os.path.exists(map_location):
        response = requests.get(faegria_map_url + "/src/assets/maps/faergria.png", stream=True)
        with open(map_location, "wb") as file:
            shutil.copyfileobj(response.raw, file)


def save_character_images(characters: pd.DataFrame, output_dir: str = "data/images"):
    project_root = Path(__file__).resolve().parent
    output_dir = project_root / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    base_url = "https://images.zetsuboushii.site/resized/dnd/characters/"
    for character_name in characters["name"]:
        character_name = character_name.lower()
        image_url = f"{base_url}{character_name}.png"
        image_path = output_dir / f"{character_name}.png"
        if image_path.exists():
            continue
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            with open(image_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Image for {character_name} saved successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading image for {character_name}: {e}")
