import globalBoolean from "./globalBoolean";
import Prompts from "./Prompts";
import HandSign from "./HandSign";
import { createElement } from "react";

function learnMode() {
    console.log("in function");
    let guided = document.getElementById("Allprompts");
    console.log("Guided button clicked");
    if (guided != null && guided != undefined && guided.childElementCount === 1) {
        guided.appendChild(<HandSign />);
    }
    }

function GuidedButton() {
    console.log("Guided button created");
    return(
        <div id="guided" className="chooseButton" onClick={learnMode}><p>GUIDED</p></div>
    );
}

export default GuidedButton;