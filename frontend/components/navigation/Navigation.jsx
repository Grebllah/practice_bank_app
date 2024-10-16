import { Button, Navbar } from 'react-bootstrap'

function Navigation(props) {
    return (
        <>
            <Navbar fixed="top" className="justify-content-end">
                <Button onClick={()=>{props.onRouteChange('authentication')}}>Sign In</Button>
                <Button onClick={()=>{
                    props.onRouteChange('authentication')
                    props.setLoginDetails({
                        email: '',
                        username: '',
                        password: ''
                    })
                    props.setAccDetails({
                        email:'',
                        username: '',
                        accountNumber: '',
                        balance: 0
                    })
                    props.setTxDetails({
                        txToAccount: '',
                        txAmount: 0,
                        txCurrency: ''
                    })
                }}>Sign Out</Button>
            </Navbar>
        </>
    )
}

export default Navigation