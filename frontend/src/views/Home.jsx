import Button from "../components/Button"
import Astuces from "../data/Astuces"

export default function Home() {
    return(
        <section id="home" className="w-full min-h-[73.8vh]">
           <div className="container m-auto flex flex-col items-center">
                <div className="text-5xl text-[#A52A2A] my-5">BEST FLAG</div>
                <div className="my-3 container">
                    <p className="mb-3 text-center"> The Best Flag !!! Et si on s'entraînait un peu sur la cryptographie et la stéganographie ?</p>
                    <p className="mb-5 text-center"> Parviendrez-vous à trouver le flag dans ce fichier <span className="text-[#A52A2A] hover:cursor-pointer">best_flag</span> ?
                    Vous aurez sûrement besoin de ces <span className="text-[#A52A2A] hover:cursor-pointer">scripts Python</span> pour la cryptographie. Mais pour la stéganographie, c'est à vous de la découvrir.</p>
                    <div className="mx-2">
                        <p className="text-4xl text-[#A52A2A] mb-3">Astuces</p>
                        {
                            Astuces().map((item, index) => (
                                <p key={index} className="mb-2"><span className=" text-[#A52A2A]">{ index + 1 }</span> - {item}</p>
                            ))
                        }
                    </div>
                </div>
                <Button>Commencer</Button>
           </div>
        </section>
    )
}