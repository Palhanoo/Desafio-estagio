import axios from 'axios';
import React, {useEffect, useState} from 'react';
import './App.css';
import Button from './components/Button';
import Card from './components/Card';

function App() {
  const [users, setUsers] = useState([])

  const buscar_dados = async () => {
    const {data } = await axios.get('http://localhost:3000');
    const dados = data;
    console.log(data)
    setUsers(dados)

  }

  // eslint-disable-next-line react-hooks/exhaustive-deps
  const handleButtonClick = () => {
    buscar_dados()
  }
  
  useEffect(() => {
    buscar_dados()
  }, [])


  return (
    <div className="App flex align-center justify-center flex-col bg-pink-900 max-h-full">
      <div className='text-black font-black'>Usuários</div>

      <Card users={users} />

      <div className='align-center p-5'>
        <Button handleChange={handleButtonClick} />
      </div>
    </div>
  );
}

export default App;
