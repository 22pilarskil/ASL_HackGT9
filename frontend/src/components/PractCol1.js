import GuidedButton from "./GuidedButton";
import UnGuidedButton from "./UnguidedButton";
import Letter from "./Letter";
import HandSign from "./HandSign";
import globalBoolean from "./globalBoolean";
import Prompts from "./Prompts";

function PractCol1() {
    return (
        <div id="col1">
        <div id="buttons">
            <GuidedButton />
            <UnGuidedButton />
        </div>
        <Prompts />
    </div>
    );
}

export default PractCol1;