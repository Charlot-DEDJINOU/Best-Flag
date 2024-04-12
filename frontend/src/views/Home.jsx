import Button from "../components/Button"
import Astuces from "../data/Astuces"
import { useNavigate } from 'react-router-dom'

export default function Home() {

    localStorage.clear()
    const navigate = useNavigate()

    return(
        <section id="home" className="w-full min-h-[47.5vh]">
           <div className="container m-auto flex flex-col items-center">
                <div className="mx-2">
                    <p className="text-4xl text-[#A52A2A] mb-3">Astuces</p>
                    {
                        Astuces().map((item, index) => (
                            <p key={index} className="mb-2"><span className=" text-[#A52A2A]">{ index + 1 }</span> - {item}</p>
                        ))
                    }
                </div>
                <Button onClick={() => navigate('/substitution')}>Commencer</Button>
            </div>
        </section>
    )
}