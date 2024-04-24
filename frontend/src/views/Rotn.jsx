import Button from "../components/Button"
import { useNavigate } from "react-router-dom"
import best from '../assets/best.png'
import { downloadImage } from "../utils/utils"

export default function Rotn() {

    const navigate = useNavigate()
    return(
        <section id="rotn" className="w-full">
            <div className="container m-auto flex flex-col items-center text-justify px-4">
                <p className="text-2xl font-medium mb-5">Algorithme ROTN</p>
                <p className="mb-3">
                    La clé que vous trouverez à cette étape est pour l'algorithme rotn. Et si on se lancait encore dans <b className="text-[#A52A2A]">la steganographie d'image ?</b> 
                </p>
                <p className="leading-relaxed text-justify mb-3"> 
                    <b className="text-[#A52A2A]">La stéganographie d'image</b> est une technique de dissimulation qui consiste à cacher des informations (texte, image, fichier, etc.) 
                    à l'intérieur d'une image sans altérer visiblement l'apparence de cette dernière. Contrairement au chiffrement qui rend les données illisibles sans la clé de déchiffrement, 
                    la stéganographie vise à rendre les données cachées invisibles à toute personne qui ne sait pas où chercher. La stéganographie d'image est utilisée dans divers domaines pour des 
                    raisons de sécurité, de confidentialité, mais aussi dans le domaine artistique pour créer des œuvres visuellement intéressantes avec des couches de significations cachées.
                </p>
                <p className="my-5">
                    Vous en avez suffisamment sur le thème en question. Maintenant passons à la pratique. Pouvez-vous extraire les informations utiles de cette image <span onClick={() => downloadImage('best.png', best)} className="text-[#A52A2A] hover:cursor-pointer">best.png</span> ?
                </p>
                <div className="flex flex-row justify-around w-96">
                    <Button onClick={() => navigate('/offset')}>Précédente</Button>
                </div>
            </div>
        </section>
    )
}