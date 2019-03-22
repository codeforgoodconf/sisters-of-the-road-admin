import { connect } from 'react-redux'

import ConformationPage from './ConfirmationPage' 


const mSTP = (state) => ({
    account: state.entities.account
})


export default connect(mSTP)(ConformationPage)