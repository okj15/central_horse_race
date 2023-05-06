import {RaceInfoType} from "@/pages/api/raceInfo";
import {RaceResultType} from "@/pages/api/raceResult";
import {JockeyResultType} from "@/pages/api/jockey";
import RaceResult from "@/components/organisms/raceResult";
import JockeyResult from "@/components/organisms/jockey";
import {useState} from "react";

import {Tab, TabList, TabPanel, Tabs} from 'react-tabs';


function Race(props: {
    raceResults: RaceResultType[],
    raceInfo: RaceInfoType | null,
    jockeyResults: JockeyResultType[]
}) {

    const [activeLink, setActiveLink] = useState("#race");

    const handleSelect = (eventKey: string | null) => {
        if (eventKey == null) return;
        setActiveLink(eventKey);
    };

    return (
        <div>
            <Tabs>
                <TabList>
                    <Tab>レース</Tab>
                    <Tab>騎手成績</Tab>
                </TabList>

                <TabPanel>
                    <RaceResult raceResults={props.raceResults}/>
                </TabPanel>
                <TabPanel>
                    <JockeyResult jockeyResults={props.jockeyResults}/>
                </TabPanel>
            </Tabs>
        </div>
    );
}

export default Race;

