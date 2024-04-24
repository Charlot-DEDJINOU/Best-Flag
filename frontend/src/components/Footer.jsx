export default function Footer() {
    return(
        <footer className="w-full bg-[#000000] flex items-center justify-center p-5">
            <div className="container flex flex-col items-center">
                <b className="text-center mb-3 text-3xl text-[#A52A2A]">BEST FLAG</b>
                <p className="text-center"> L’être humain à le potentiel de devenir quelque chose d’autre - David Goggins</p>
                <div className="copyright my-4">
                    &copy; Copyright <strong><span>Best Flag </span></strong>All Rights Reserved 
                </div>
                <div>
                    Created by
                    <a href="https://charlot-dedjinou.vercel.app" className="font-bold"> Charlot DEDJINOU</a>
                </div>
            </div>
        </footer>
    )
}