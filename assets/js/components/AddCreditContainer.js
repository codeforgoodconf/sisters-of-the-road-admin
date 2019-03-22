import { connect } from 'react-redux';

import AddCreditPage from './AddCreditPage';

import { credit } from '../actions/account_actions'

const mapStateToProps = (state) => ({
    account: state.entities.account,
    error: state.errors.buyError,
})

const mapDispatchToProps = dispatch => ({
    action: (account, amount) => dispatch(credit(account, amount))
})

export default connect(mapStateToProps, mapDispatchToProps)(AddCreditPage)