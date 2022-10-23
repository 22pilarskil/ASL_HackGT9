import PractCol1 from "../components/PractCol1";
import PractCol2 from "../components/PractCol2";
import Directions from "../components/Directions";
function Practice() {

    return (
        <div id="allPract">
            <div id="practHeading">
            <h1>PRACTICE</h1>
            </div>
            <div id="practice">
            <PractCol1/>
            <PractCol2/>
            </div>
        </div>
       
    );
}

export default Practice;