import React, { Component } from 'react';


class SearchPage extends Component {
    constructor (props) {
        super(props);
        this.state = {
            accounts:this.props.accounts,
            searchQuery:this.props.searchQuery
        };
        this.onSearchQueryValueChangeNotify = this.props.onSearchQueryValueChangeNotify.bind(this);
    }

    onSearchChange (value) {
        this.setState({searchQuery: value});
        this.onSearchQueryValueChangeNotify(this.state.searchQuery);
    }
    UNSAFE_componentWillReceiveProps(nextProps){
        if (this.props != nextProps){
            this.setState({
                searchQuery: this.props.searchQuery
            });
        }
    }

    componentDidUpdate(prevProps) {
      
    ;}

    searchAccounts () {
        var sk = $('#searchbar input[placeholder="search accounts"]').value;
        if (sk == undefined) sk = $('#searchbar input[placeholder="search accounts"]').val();
        if (typeof this.state.searchQuery == "undefined")
            this.state.searchQuery = sk;
        axios.get('/account/search?q=' + this.state.searchQuery).then((response) => {
            console.log("q=" + this.state.searchQuery)
            let accounts = [];
            response.data.forEach((account, index) => {
                accounts.push({
                    name: account.name,
                    id: account.account_id,
                    lastCredit: account.last_add,
                    lastMeal: account.last_subtract,
                    currentCredit: Number(account.balance)
                });
            });
            // Sort the account objects by name
            // https://stackoverflow.com/questions/6712034/sort-array-by-firstname-alphabetically-in-javascript
            accounts.sort(function(a, b){
                if (a.name.toLowerCase() < b.name.toLowerCase()) //sort string ascending
                    return -1;
                if (a.name.toLowerCase() > b.name.toLowerCase())
                    return 1;
                return 0; //default return value (no sorting)
                });
            this.setState({accounts: accounts});
        });
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
                        <li class="stripe-dark pv2 pa3"
                            onClick={() => this.props.switchView('accountpage', account)}
                            key={account.id}>
                            <p> {account.name} </p>
                            <p> {account.balance} </p>
                            <p>Last credit: {account.lastCredit}</p>
                            <p>Last purchase: {account.lastMeal}</p>
                        </li>
                    )}
                  </ul>
                </div>

            </div>
         );
    }
}

export default SearchPage;
