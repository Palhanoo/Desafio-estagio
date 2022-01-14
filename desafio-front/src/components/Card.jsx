import React from 'react'

const Card = (users) => {

    const user = users.users
    console.log(user)
    
    return (
        <div className='grid grid-cols-4 gap-3 max-h-full p-2'>
            {user.map((item, idx)=> (
                <div className='border h-36 rounded flex' key={idx}>
                    <div className='m-2' >
                        <img className='border rounded' src={item.picture.large} alt='user-pic' />
                    </div>
                    <div>
                        <div className='m-3'>Nome: {item.name.first} {item.name.last}</div>
                        <div className='m-3'>Idade: {item.dob.age}</div>
                        <div className='m-3'>Cidade: {item.location.country}</div>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default Card
