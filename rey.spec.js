/// <reference types="cypress" />

describe('Search feature', function() {
    it('Search Pikachu di menu pencarian', function() {
        cy.visit("https://www.pokemon.com/us/")
        .wait(5000)
        cy.get('#onetrust-close-btn-container > .onetrust-close-btn-handler').click()
        .wait(2000)
        cy.get('.search > .icon').click()
        .wait(2000)
        cy.get('#site-search-widget-term').type('Pikachu',100)
        .wait(2000)
        cy.get(':nth-child(1) > a > .search-result-info-wrapper > h3').click()
        cy.get('.pokedex-pokemon-pagination-title > div').then(($el) => {
            let Actual = $el.text();
            let Expected = '\n      Pikachu\n      #025\n    '
            assert.equal(Actual, Expected, '== Harus sama dengan expected result');
        })
        cy.scrollTo(0, 1000)
        .wait(2000)
        cy.get('.content-block-half > .button').click()
        .wait(2000)
        let height = 1800
        cy.scrollTo(0, 1800)
        .wait(2000)
        cy.get('#loadMore > .button-lightblue').click()
        .wait(2000)
        for (let i = 1; i <= 10; i++) {
            let val = height * i
            cy.scrollTo(0, val)
            .wait(2000)
        }
    })
})
