import React, { Component } from 'react';


class SearchPage extends Component {
    constructor (props) {
        super(props);
        this.state = {
            
        };
        this.onSearchChange = this.onSearchChange.bind(this)
    }

    componentWillReceiveProps(oldProps) {
        if (this.props.searchQuery !== oldProps.searchQuery) {
            this.setState({loaded: true})
        }
    }

    onSearchChange (value) {
        this.setState({searchQuery: value});
    }
    
    handleSubmit() {
        this.props.requestSearchQuery(this.state.searchQuery)
    }

    render () {

        var {
            accounts,
            searchQuery
        } = this.state;

       if (typeof accounts == "undefined") accounts =[];
       if (typeof searchQuery == "undefined") searchQuery = '';
        return (
            <div class="SearchPage pa4">
                <div id="searchbar" class="flex">
                <input class="h3 f3 pl2 mr2 w-75 b--purple ttu oswald br0"
                         type="text"
                         placeholder="search accounts"
                         onChange={(event) => this.onSearchChange(event.target.value)}/>
                  <input class="h3 f4 ph0 w-25 b--purple white bg-purple mb2 oswald"
                         type="submit"
                         value="SEARCH"
                         onClick={() => this.searchAccounts(searchQuery)}
                         />
                </div>

                <div id='results'>
                  <ul class="list pa0">
                    {accounts.map((account) =>
                        <li class="bg-light-gray pv2 pa3 mb3 b--solid br1 b--moon-gray flex items-center"
                            onClick={() => this.props.switchView('accountpage', account)}
                            key={account.id}>
                            <span class="flex-auto">
                                <p> {account.name} </p>
                                <p> {account.balance} </p>
                                <p>Last credit: {account.lastCredit}</p>
                                <p>Last purchase: {account.lastMeal}</p>
                            </span>
                            <span class="f1 silver">&rsaquo;</span>
                        </li>
                    )}
                  </ul>
                </div>

            </div>
         );
    }
}

export default SearchPage;
