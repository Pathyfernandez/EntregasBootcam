
    function pizzaOven(tipoCorteza, tipoSalsa, quesos, salsas) {
        var pizza = {
        tipoCorteza: tipoCorteza,
        tipoSalsa: tipoSalsa,
        quesos: quesos,
        salsas: salsas
        };
        return pizza;
    }

var pizza1 = pizzaOven("tradicional", "estilo Chicago",  ["mozzarella"], ["pepperoni", "salchicha"]);
console.table(pizza1);

var pizza2 = pizzaOven("lanzada a mano", "marinara", ["mozzarella", "feta"], ["champiñones", "aceitunas", "cebollas"]);
console.table(pizza2);

// Crea 2 pizzas más con los ingredientes que quieras
var pizza3 = pizzaOven("delgada", "barbacoa", ["cheddar", "gouda"], ["pollo", "pimientos"]);
console.table(pizza3);

var pizza4 = pizzaOven("gruesa", "alfredo", ["parmesano", "ricotta"], ["espinacas", "tomates secos"]);
console.table(pizza4)



