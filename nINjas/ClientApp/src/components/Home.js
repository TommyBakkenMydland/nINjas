import React, { Component } from 'react';
import logo from './logo.png';
import Form from 'react-bootstrap/Form';
export class Home extends Component {
  static displayName = Home.name;
  
  constructor(props) {
    super(props);
    this.state = { shoppingLists: [], loading: true };
  }

  static renderShoppingListTable(shoppingLists) {
    return (
      <table class="center">
        <thead>
          <tr>
            <th>Matvare</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {shoppingLists.map(shoppingList =>
            <tr key={shoppingList.date}>
              <td>{shoppingList.name}</td>   
              <td>      <Form.Check 
        type="switch"
        id="custom-switch"

      /></td>         
            </tr>
          )}
        </tbody>
      </table>
      
    );
  }
  componentDidMount() {
    this.populateShoppingListData();
  }
  render () {
    let contents = this.state.loading
    ? <p><em>Loading...</em></p>
    : Home.renderShoppingListTable(this.state.shoppingLists)

    return (
      <div class="center">
        <img src={logo} alt="Logo" className="logo"/>
        {contents}
      </div>
    );
  }

  async populateShoppingListData() {
    const response = await fetch('shoppinglist');
    const data = await response.json();
    this.setState({ shoppingLists: data, loading: false });
  }
}
