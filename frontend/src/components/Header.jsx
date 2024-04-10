export default function Header() {
    return(
        <header>
            <div className="container m-auto flex flex-col items-center">
                <div className="text-5xl text-[#A52A2A] my-5">BEST FLAG</div>
                <div className="container my-3">
                    <p className="mb-3 text-center"> The Best Flag !!! Et si on s'entraînait un peu sur la cryptographie et la stéganographie ?</p>
                    <p className="mb-5 text-center"> Parviendrez-vous à trouver le flag dans ce fichier <span className="text-[#A52A2A] hover:cursor-pointer">best_flag</span> ?
                    Vous aurez sûrement besoin de ces <span className="text-[#A52A2A] hover:cursor-pointer">scripts Python</span> pour la cryptographie. Mais pour la stéganographie, c'est à vous de la découvrir.</p>
                </div>
            </div>
        </header>
    )
}