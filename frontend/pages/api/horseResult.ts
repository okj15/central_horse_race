export async function fetchHorseResult(horseId: string) {
    if (horseId === undefined) {
        return undefined;
    }

    const response = await fetch(`http://localhost:8080/api/racing_horse/detail/${horseId}/`);
    const data: HorseResponse = await response.json();

    const raceResults: RaceResultType[] = [];
    for (const obj of data.results) {
        raceResults.push({
            id: obj.id,
            bracket: obj.bracket,
            horseNumber: obj.horse_number,
            gender: obj.get_gender_display,
            age: obj.age,
            jockeyWeight: obj.jockey_weight,
            raceTime: obj.race_time,
            popularity: obj.popularity,
            odds: obj.odds,
            rank: obj.rank,
            trainingCenter: obj.get_training_center_display,
            jokeyName: obj.jockey.name
        });
    }

    return {
        id: data.id,
        name: data.name,
        ownerName: data.owner.name,
        results: raceResults
    };
}


type OwnerResponse = {
    id: number;
    name: string;
}

type JockeyResponse = {
    id: number;
    name: string;
}

type RaceResultResponse = {
    id: number;
    bracket: number;
    horse_number: number;
    get_gender_display: string;
    age: number;
    jockey_weight: number;
    race_time: string;
    popularity: number;
    odds: number;
    rank: number;
    get_training_center_display: string;
    jockey: JockeyResponse;
}

export type RaceResultType = {
    id: number;
    bracket: number;
    horseNumber: number;
    gender: string;
    age: number;
    jockeyWeight: number;
    raceTime: string;
    popularity: number;
    odds: number;
    rank: number;
    trainingCenter: string;
    jokeyName: string;
}

type HorseResponse = {
    id: number;
    name: string;
    owner: OwnerResponse
    results: RaceResultResponse[];
}

export type HorseResultType = {
    id: number;
    name: string;
    ownerName: string;
    results: RaceResultType[];
}