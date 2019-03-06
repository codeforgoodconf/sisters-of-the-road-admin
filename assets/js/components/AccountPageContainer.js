import { connect } from 'react-redux';

import AccountPage from './AccountPage'


const mapStateToProps = (state) => ({
    account: state.entities.account
})


export default connect(mapStateToProps)(AccountPage)