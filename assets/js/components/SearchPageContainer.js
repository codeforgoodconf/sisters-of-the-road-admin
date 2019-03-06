import { connect } from 'react-redux';

import SearchPage from './SearchPage'
import { requestSearchQuery } from '../actions/account_actions'


const mapStateToProps = (state) => ({
    searchQuery: state.entities.searchQuery 
})

const mapDispatchToProps = () => dispatch => ({
    requestSearchQuery: (searchQuery) => dispatch(requestSearchQuery(searchQuery))
})

export default connect(mapStateToProps, mapDispatchToProps)(SearchPage)