import styled from "styled-components"
import Categories from './Categories'
import Products from './Products'
import MainPageFilterButtons from './MainPageFilterButtons'
import Slider from './Slider'
import React from 'react'

{/*background-color: pink*/}
const BodyContainer = styled.div`
    width: 100%;
    padding-top: 60px;
    padding-bottom: 150px;
    padding-right: 0px;
    display: flex;
    justify-content: space-between;
    flex-direction: row;
    background-color: #282c34;
    align-items: stretch;
`;

const LeftContainer = styled.div`
    width: 33%;
    padding-left: 80px;
    padding-right: 10px;
    float: right;
    justify-content: space-between;
`;

const RightContainer = styled.div`
    width: 67%;
    padding-left: 40px;
    padding-right: 0px;
    display:flex;
    flex-direction: column;
`;

const Body = ({onAddToCart}) => {
  return (
    <BodyContainer>
      <LeftContainer>
        <Categories/>
      </LeftContainer>
      <RightContainer>
        <Slider></Slider>
        <MainPageFilterButtons/>
        <Products onAddToCart={onAddToCart}/>
      </RightContainer>
    </BodyContainer>
  )
}

export default Body