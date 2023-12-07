{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pymongo\n",
    "import pandas as pd\n",
    "from bson import ObjectId\n",
    "\n",
    "client = pymongo.MongoClient(\"mongodb://localhost:27017\")\n",
    "db = client['plantillas_barsa_2010']\n",
    "collection = db['lesiones_barsa_20']\n",
    "\n",
    "target_id = ObjectId(\"656886b8c42e904eaef804b9\") #Cambiando el Id de cada uno, tendré la plantilla correspondiente. \n",
    "query = {\"_id\": target_id}\n",
    "data_from_mongo = collection.find_one(query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Extraer la información necesaria.\n",
    "\n",
    "data = []\n",
    "\n",
    "for e in range(len(data_from_mongo_2)):\n",
    "    for i in range(len(data_from_mongo_2[e]['response'])):\n",
    "        \n",
    "            \n",
    "        player_data = data_from_mongo_2 [e]['response'][i]['player']\n",
    "        team_data = data_from_mongo_2 [e] ['response'] [i] ['team']\n",
    "        fixture  = data_from_mongo_2 [e] ['response'] [i] ['fixture']\n",
    "        league = data_from_mongo_2 [e] ['response'] [i] ['league']\n",
    "\n",
    "        player_info = {\n",
    "            'id':player_data ['id'],\n",
    "            'name': player_data['name'],\n",
    "            'type': player_data ['type'],\n",
    "            'reason': player_data ['reason'],\n",
    "            'team': team_data ['name'],\n",
    "            'fixture': fixture ['date'],\n",
    "            'league': league ['name']\n",
    "        }\n",
    "\n",
    "        data.append(player_info)\n",
    "\n",
    "# Create a DataFrame\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# Print the DataFrame\n",
    "lesionados_2020 = df\n",
    "\n",
    "lesionados_2020"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
