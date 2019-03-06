import React, { Component } from 'react';

import AccountListItem from './AccountItem'


class SearchPage extends Component {
    constructor (props) {
        super(props);
        this.state = {
            
        };
        this.onSearchChange = this.onSearchChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
        this.handleSelect = this.handleSelect.bind(this)
    }

    componentWillReceiveProps(oldProps) {
        if (this.props.searchQuery !== oldProps.searchQuery) {
            this.setState({loaded: true})
        }

        if (this.props.account !== oldProps.account) {
            this.props.history.push('/account')
        }
    }

    onSearchChange (e) {
        this.setState({searchQuery: e.target.value});
    }
    
    handleSubmit() {
        this.props.requestSearchQuery(this.state.searchQuery)
    }

    handleSelect(account) {
        return () => {
            this.props.recieveAccount(account)
        }
    }

    render () {
        
        let accounts = (this.props.searchQuery).map(account => <AccountListItem account={account} action={this.handleSelect(account)} key={account.id}  />)

        return (
            <div className="SearchPage pa4">
                <div id="searchbar" className="flex">
                <input className="h3 f3 pl2 mr2 w-75 b--purple ttu oswald br0"
                         type="text"
                         placeholder="search accounts"
                         onChange={this.onSearchChange}/>
                  <input className="h3 f4 ph0 w-25 b--purple white bg-purple mb2 oswald"
                         type="submit"
                         value="SEARCH"
                         onClick={this.handleSubmit}
                         />
                </div>

                <div id='results'>
                  <ul className="list pa0">
                    {accounts}
                  </ul>
                </div>

            </div>
         );
    }
}

export default SearchPage;
