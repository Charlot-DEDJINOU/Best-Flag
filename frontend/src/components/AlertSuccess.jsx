export default function AlertSuccess({ message }) {
    return (
        <div className="w-full px-4 py-2 rounded-md border font-bold border-green-500 bg-green-100 text-green-700 mb-3">
            {message}
        </div>
    );
}