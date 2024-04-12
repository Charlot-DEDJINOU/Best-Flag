import { useNavigate } from "react-router-dom"
import Button from "../components/Button"
import DevinettesData from "../data/DevinettesData"
import { Redirect } from "../utils/utils"

export default function Aes() {

    localStorage.clear()
    const navigate = useNavigate()

    return(
        <section id="aes" className="w-full min-h-[47.5vh]">
            <div className="container m-auto flex flex-col items-center text-justify px-4">
                <p className="text-2xl font-medium mb-5">Algorithme AES</p>
                <p className="mb-3">
                    La clé que vous trouverez à cette étape est pour l'algorithme AES. Et si on commençait par <b className="text-[#A52A2A]">jouer au devinettes</b> ?
                </p>
                <div className="mx-2 container">
                    <p className="text-2xl text-[#A52A2A] mb-3">Quelques devinettes</p>
                    {
                        DevinettesData().map((item, index) => (
                            <p key={index} className="mb-2"><span className=" text-[#A52A2A]">{ index + 1 }</span> - {item}</p>
                        ))
                    }
                </div>
                <p className="my-3">
                    Tu as trouvé les réponses à ces petites énigmes ? Ouais Ouais, je viens de dire petites énigmes, montre-nous ce que tu vaux en devinettes sur <b className="text-[#A52A2A] hover:cursor-pointer" onClick={() => Redirect("https://animated-hbd-nlp-js.vercel.app")}>ce site</b> !
                </p>
                <div className="flex flex-row justify-around w-96">
                    <Button onClick={() => navigate('/ascii')}>Précédente</Button>
                    <Button onClick={() => navigate('/rotn')}>Suivante</Button>
                </div>
            </div>
        </section>
    )
}