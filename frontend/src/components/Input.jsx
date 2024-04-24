import React from 'react';

export default function Input ({ label, type, name, value, placeholder, onChange }) {
  return (
    <div className='w-full mb-3 flex flex-col'>
        <label className='mb-1'>{label}<span className='text-[#A52A2A]'>*</span></label>
        <input
            name={name}
            type={type}
            placeholder={placeholder}
            onChange={onChange}
            value={value}
            className="w-full px-4 py-2 rounded-md border text-black bg-white border-gray-300 focus:outline-none focus:border-[#A52A2A]"
        />
    </div>
  );
};