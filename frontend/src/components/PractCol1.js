import GuidedButton from "./GuidedButton";
import UnGuidedButton from "./UnguidedButton";
import Letter from "./Letter";
import HandSign from "./HandSign";

function PractCol1() {
    return (
        <div id="col1">
            <div id="buttons">
                <GuidedButton />
                <UnGuidedButton />
            </div>
            <div id="letterDisplay">
                <Letter data={""}></Letter>
            </div>
            <div id="handDisplay">
                <HandSign data={""}></HandSign>
            </div>

        </div>
    );
}

export default PractCol1;