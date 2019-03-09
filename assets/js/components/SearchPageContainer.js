import { connect } from 'react-redux';

import SearchPage from './SearchPage'
import { requestSearchQuery, recieveAccount, clearSearchQuery } from '../actions/account_actions'


const mapStateToProps = (state) => ({
    searchQuery: state.entities.searchQuery,
    account: state.entities.account
})

const mapDispatchToProps = () => dispatch => ({
    requestSearchQuery: (searchQuery) => dispatch(requestSearchQuery(searchQuery)),
    recieveAccount: (account) => dispatch(recieveAccount(account))
})

export default connect(mapStateToProps, mapDispatchToProps)(SearchPage)