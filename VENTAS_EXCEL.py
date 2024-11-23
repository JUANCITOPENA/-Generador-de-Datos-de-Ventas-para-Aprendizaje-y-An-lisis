import random
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
import os

# Definición global de productos_base
productos_base = {
    "Comida Rápida": [
        {"nombre": "Hamburguesa", "categoria": "Comida Rápida", "precio_compra": 50, "precio_venta": 90, "stock": 500},
        {"nombre": "Pizza", "categoria": "Comida Rápida", "precio_compra": 80, "precio_venta": 150, "stock": 300},
        {"nombre": "Hot Dog", "categoria": "Comida Rápida", "precio_compra": 30, "precio_venta": 60, "stock": 400},
        {"nombre": "Papas Fritas", "categoria": "Comida Rápida", "precio_compra": 20, "precio_venta": 40, "stock": 600},
        {"nombre": "Refresco", "categoria": "Bebida", "precio_compra": 15, "precio_venta": 30, "stock": 800},
        {"nombre": "Alitas de Pollo", "categoria": "Comida Rápida", "precio_compra": 60, "precio_venta": 110, "stock": 350},
        {"nombre": "Nuggets", "categoria": "Comida Rápida", "precio_compra": 40, "precio_venta": 75, "stock": 400},
        {"nombre": "Tacos", "categoria": "Comida Rápida", "precio_compra": 35, "precio_venta": 70, "stock": 450},
        {"nombre": "Sandwich", "categoria": "Comida Rápida", "precio_compra": 25, "precio_venta": 50, "stock": 500},
        {"nombre": "Ensalada César", "categoria": "Comida Rápida", "precio_compra": 30, "precio_venta": 60, "stock": 300},
        {"nombre": "Smoothie", "categoria": "Bebida", "precio_compra": 25, "precio_venta": 50, "stock": 400},
        {"nombre": "Café Helado", "categoria": "Bebida", "precio_compra": 20, "precio_venta": 40, "stock": 350},
        {"nombre": "Empanadas", "categoria": "Comida Rápida", "precio_compra": 15, "precio_venta": 30, "stock": 500},
        {"nombre": "Churros", "categoria": "Postre", "precio_compra": 10, "precio_venta": 20, "stock": 700},
        {"nombre": "Brownie", "categoria": "Postre", "precio_compra": 25, "precio_venta": 50, "stock": 300},
        {"nombre": "Helado de Vainilla", "categoria": "Postre", "precio_compra": 20, "precio_venta": 40, "stock": 400},
        {"nombre": "Wrap de Pollo", "categoria": "Comida Rápida", "precio_compra": 40, "precio_venta": 80, "stock": 300},
        {"nombre": "Sushi Roll", "categoria": "Comida Rápida", "precio_compra": 50, "precio_venta": 100, "stock": 200},
        {"nombre": "Quesadilla", "categoria": "Comida Rápida", "precio_compra": 30, "precio_venta": 60, "stock": 400},
        {"nombre": "Cheesecake", "categoria": "Postre", "precio_compra": 40, "precio_venta": 80, "stock": 250},
        {"nombre": "Batido de Fresa", "categoria": "Bebida", "precio_compra": 25, "precio_venta": 50, "stock": 300},
        {"nombre": "Malteada", "categoria": "Bebida", "precio_compra": 35, "precio_venta": 70, "stock": 250},
        {"nombre": "Mozzarella Sticks", "categoria": "Comida Rápida", "precio_compra": 30, "precio_venta": 60, "stock": 350},
        {"nombre": "Burrito", "categoria": "Comida Rápida", "precio_compra": 45, "precio_venta": 90, "stock": 400},
        {"nombre": "Crepa de Nutella", "categoria": "Postre", "precio_compra": 30, "precio_venta": 60, "stock": 200},
        {"nombre": "Donas", "categoria": "Postre", "precio_compra": 15, "precio_venta": 30, "stock": 600},
        {"nombre": "ChocoFrappé", "categoria": "Bebida", "precio_compra": 30, "precio_venta": 60, "stock": 350},
        {"nombre": "Patacones", "categoria": "Comida Rápida", "precio_compra": 20, "precio_venta": 40, "stock": 450},
        {"nombre": "Pizza Calzone", "categoria": "Comida Rápida", "precio_compra": 70, "precio_venta": 140, "stock": 150},
        {"nombre": "Costillas BBQ", "categoria": "Comida Rápida", "precio_compra": 100, "precio_venta": 180, "stock": 200}
    ],
    "Supermercado": [
        {"nombre": "Arroz", "categoria": "Alimentos", "precio_compra": 25, "precio_venta": 40, "stock": 1000},
        {"nombre": "Aceite", "categoria": "Alimentos", "precio_compra": 50, "precio_venta": 85, "stock": 500},
        {"nombre": "Leche", "categoria": "Lácteos", "precio_compra": 30, "precio_venta": 55, "stock": 800},
        {"nombre": "Cereal", "categoria": "Desayuno", "precio_compra": 20, "precio_venta": 40, "stock": 600},
        {"nombre": "Jugo", "categoria": "Bebidas", "precio_compra": 15, "precio_venta": 30, "stock": 700},
        {"nombre": "Pan", "categoria": "Panadería", "precio_compra": 10, "precio_venta": 20, "stock": 400},
        {"nombre": "Harina", "categoria": "Alimentos", "precio_compra": 18, "precio_venta": 30, "stock": 1000},
        {"nombre": "Queso", "categoria": "Lácteos", "precio_compra": 50, "precio_venta": 75, "stock": 300},
        {"nombre": "Huevos", "categoria": "Alimentos", "precio_compra": 60, "precio_venta": 100, "stock": 200},
        {"nombre": "Mantequilla", "categoria": "Lácteos", "precio_compra": 40, "precio_venta": 70, "stock": 400},
        {"nombre": "Pollo", "categoria": "Carnes", "precio_compra": 80, "precio_venta": 120, "stock": 250},
        {"nombre": "Carne de res", "categoria": "Carnes", "precio_compra": 120, "precio_venta": 180, "stock": 200},
        {"nombre": "Pescado", "categoria": "Carnes", "precio_compra": 100, "precio_venta": 150, "stock": 150},
        {"nombre": "Manzanas", "categoria": "Frutas", "precio_compra": 25, "precio_venta": 40, "stock": 300},
        {"nombre": "Plátanos", "categoria": "Frutas", "precio_compra": 10, "precio_venta": 15, "stock": 1000},
        {"nombre": "Naranjas", "categoria": "Frutas", "precio_compra": 20, "precio_venta": 35, "stock": 400},
        {"nombre": "Tomates", "categoria": "Verduras", "precio_compra": 15, "precio_venta": 25, "stock": 500},
        {"nombre": "Cebollas", "categoria": "Verduras", "precio_compra": 18, "precio_venta": 30, "stock": 600},
        {"nombre": "Papas", "categoria": "Verduras", "precio_compra": 12, "precio_venta": 20, "stock": 700},
        {"nombre": "Zanahorias", "categoria": "Verduras", "precio_compra": 10, "precio_venta": 18, "stock": 650},
        {"nombre": "Refresco", "categoria": "Bebidas", "precio_compra": 25, "precio_venta": 45, "stock": 800},
        {"nombre": "Agua embotellada", "categoria": "Bebidas", "precio_compra": 10, "precio_venta": 20, "stock": 1000},
        {"nombre": "Galletas", "categoria": "Snacks", "precio_compra": 15, "precio_venta": 30, "stock": 500},
        {"nombre": "Chocolate", "categoria": "Snacks", "precio_compra": 20, "precio_venta": 35, "stock": 400},
        {"nombre": "Café", "categoria": "Desayuno", "precio_compra": 50, "precio_venta": 80, "stock": 300},
        {"nombre": "Té", "categoria": "Desayuno", "precio_compra": 30, "precio_venta": 50, "stock": 400},
        {"nombre": "Azúcar", "categoria": "Alimentos", "precio_compra": 20, "precio_venta": 35, "stock": 700},
        {"nombre": "Sal", "categoria": "Alimentos", "precio_compra": 10, "precio_venta": 15, "stock": 800},
        {"nombre": "Pasta", "categoria": "Alimentos", "precio_compra": 25, "precio_venta": 40, "stock": 900},
        {"nombre": "Salsa de tomate", "categoria": "Condimentos", "precio_compra": 15, "precio_venta": 30, "stock": 600},
        {"nombre": "Mayonesa", "categoria": "Condimentos", "precio_compra": 25, "precio_venta": 45, "stock": 500},
        {"nombre": "Ketchup", "categoria": "Condimentos", "precio_compra": 20, "precio_venta": 35, "stock": 400},
        {"nombre": "Detergente", "categoria": "Limpieza", "precio_compra": 30, "precio_venta": 55, "stock": 500},
        {"nombre": "Jabón", "categoria": "Limpieza", "precio_compra": 15, "precio_venta": 25, "stock": 700},
        {"nombre": "Shampoo", "categoria": "Higiene", "precio_compra": 40, "precio_venta": 70, "stock": 300},
        {"nombre": "Crema dental", "categoria": "Higiene", "precio_compra": 25, "precio_venta": 45, "stock": 400},
        {"nombre": "Pañales", "categoria": "Higiene", "precio_compra": 80, "precio_venta": 120, "stock": 200},
        {"nombre": "Servilletas", "categoria": "Limpieza", "precio_compra": 10, "precio_venta": 18, "stock": 600},
        {"nombre": "Cloro", "categoria": "Limpieza", "precio_compra": 20, "precio_venta": 35, "stock": 400},
        {"nombre": "Papel higiénico", "categoria": "Limpieza", "precio_compra": 25, "precio_venta": 40, "stock": 500},
        {"nombre": "Jabón líquido", "categoria": "Limpieza", "precio_compra": 30, "precio_venta": 55, "stock": 300},
        {"nombre": "Mermelada", "categoria": "Desayuno", "precio_compra": 20, "precio_venta": 40, "stock": 400},
        {"nombre": "Miel", "categoria": "Desayuno", "precio_compra": 35, "precio_venta": 60, "stock": 300},
        {"nombre": "Chicles", "categoria": "Snacks", "precio_compra": 5, "precio_venta": 10, "stock": 1000},
        {"nombre": "Sopa instantánea", "categoria": "Alimentos", "precio_compra": 12, "precio_venta": 20, "stock": 800},
        {"nombre": "Yogur", "categoria": "Lácteos", "precio_compra": 20, "precio_venta": 35, "stock": 500},
        {"nombre": "Helado", "categoria": "Postres", "precio_compra": 50, "precio_venta": 80, "stock": 250}
    ],

      "Tienda Gamer": [
        {"nombre": "Control Xbox Series X", "categoria": "Accesorios", "precio_compra": 1500, "precio_venta": 2500, "stock": 100},
        {"nombre": "PlayStation 5 Digital", "categoria": "Consolas", "precio_compra": 18000, "precio_venta": 22000, "stock": 50},
        {"nombre": "Mouse Razer DeathAdder", "categoria": "Accesorios", "precio_compra": 500, "precio_venta": 800, "stock": 200},
        {"nombre": "Auriculares HyperX Cloud", "categoria": "Accesorios", "precio_compra": 700, "precio_venta": 1300, "stock": 150},
        {"nombre": "Teclado Mecánico RGB", "categoria": "Accesorios", "precio_compra": 1200, "precio_venta": 1800, "stock": 120},
        {"nombre": "Nintendo Switch OLED", "categoria": "Consolas", "precio_compra": 15000, "precio_venta": 18000, "stock": 40},
        {"nombre": "Xbox Series S", "categoria": "Consolas", "precio_compra": 14000, "precio_venta": 16500, "stock": 45},
        {"nombre": "Silla Gamer Pro", "categoria": "Mobiliario", "precio_compra": 4500, "precio_venta": 6000, "stock": 30},
        {"nombre": "Mousepad XL RGB", "categoria": "Accesorios", "precio_compra": 400, "precio_venta": 700, "stock": 180},
        {"nombre": "Webcam 1080p", "categoria": "Streaming", "precio_compra": 800, "precio_venta": 1200, "stock": 90},
        {"nombre": "Micrófono Blue Yeti", "categoria": "Streaming", "precio_compra": 2500, "precio_venta": 3500, "stock": 40},
        {"nombre": "Control PS5 DualSense", "categoria": "Accesorios", "precio_compra": 1600, "precio_venta": 2600, "stock": 110},
        {"nombre": "Memoria RAM RGB 16GB", "categoria": "Componentes", "precio_compra": 2000, "precio_venta": 2800, "stock": 75},
        {"nombre": "GPU RTX 3060", "categoria": "Componentes", "precio_compra": 12000, "precio_venta": 15000, "stock": 25},
        {"nombre": "Monitor 144Hz 27\"", "categoria": "Pantallas", "precio_compra": 8000, "precio_venta": 10500, "stock": 35},
        {"nombre": "Capture Card Elgato", "categoria": "Streaming", "precio_compra": 4000, "precio_venta": 5500, "stock": 20},
        {"nombre": "Base Refrigerante Laptop", "categoria": "Accesorios", "precio_compra": 600, "precio_venta": 900, "stock": 140},
        {"nombre": "Joy-Con Nintendo Switch", "categoria": "Accesorios", "precio_compra": 1800, "precio_venta": 2500, "stock": 80},
        {"nombre": "Fuente 750W Gold", "categoria": "Componentes", "precio_compra": 2500, "precio_venta": 3500, "stock": 45},
        {"nombre": "Gabinete RGB", "categoria": "Componentes", "precio_compra": 1800, "precio_venta": 2600, "stock": 55},
        {"nombre": "Disco SSD 1TB", "categoria": "Componentes", "precio_compra": 2200, "precio_venta": 3000, "stock": 65},
        {"nombre": "Procesador Ryzen 7", "categoria": "Componentes", "precio_compra": 8500, "precio_venta": 10500, "stock": 30},
        {"nombre": "Cable HDMI 2.1", "categoria": "Accesorios", "precio_compra": 300, "precio_venta": 500, "stock": 250},
        {"nombre": "Ring Light LED", "categoria": "Streaming", "precio_compra": 900, "precio_venta": 1400, "stock": 70},
        {"nombre": "Tarjeta PSN $50", "categoria": "Digital", "precio_compra": 1200, "precio_venta": 1500, "stock": 300}
    ],
   
    "Ventas Autos": [
        {"nombre": "Toyota Corolla 2023", "categoria": "Autos", "precio_compra": 500000, "precio_venta": 600000, "stock": 5},
        {"nombre": "Honda Civic 2022", "categoria": "Autos", "precio_compra": 450000, "precio_venta": 520000, "stock": 3},
        {"nombre": "Nissan Altima 2021", "categoria": "Autos", "precio_compra": 400000, "precio_venta": 470000, "stock": 2},
        {"nombre": "Ford Focus 2023", "categoria": "Autos", "precio_compra": 420000, "precio_venta": 490000, "stock": 4},
        {"nombre": "Chevrolet Spark 2022", "categoria": "Autos", "precio_compra": 300000, "precio_venta": 350000, "stock": 6},
        {"nombre": "Hyundai Elantra 2023", "categoria": "Autos", "precio_compra": 480000, "precio_venta": 550000, "stock": 3},
        {"nombre": "Kia Rio 2022", "categoria": "Autos", "precio_compra": 350000, "precio_venta": 420000, "stock": 4},
        {"nombre": "Toyota Camry 2023", "categoria": "Autos", "precio_compra": 550000, "precio_venta": 650000, "stock": 2},
        {"nombre": "Mazda 3 2022", "categoria": "Autos", "precio_compra": 460000, "precio_venta": 540000, "stock": 3},
        {"nombre": "Volkswagen Jetta 2023", "categoria": "Autos", "precio_compra": 490000, "precio_venta": 580000, "stock": 4},
        {"nombre": "Honda Accord 2023", "categoria": "Autos", "precio_compra": 580000, "precio_venta": 680000, "stock": 2},
        {"nombre": "Nissan Sentra 2022", "categoria": "Autos", "precio_compra": 420000, "precio_venta": 500000, "stock": 5},
        {"nombre": "Hyundai Accent 2023", "categoria": "Autos", "precio_compra": 380000, "precio_venta": 450000, "stock": 4},
        {"nombre": "Toyota Yaris 2022", "categoria": "Autos", "precio_compra": 340000, "precio_venta": 410000, "stock": 6},
        {"nombre": "Kia Forte 2023", "categoria": "Autos", "precio_compra": 430000, "precio_venta": 510000, "stock": 3},
        {"nombre": "Chevrolet Cruze 2022", "categoria": "Autos", "precio_compra": 440000, "precio_venta": 520000, "stock": 4},
        {"nombre": "Honda Fit 2022", "categoria": "Autos", "precio_compra": 360000, "precio_venta": 430000, "stock": 5},
        {"nombre": "Nissan Versa 2023", "categoria": "Autos", "precio_compra": 370000, "precio_venta": 440000, "stock": 4},
        {"nombre": "Mazda 2 2022", "categoria": "Autos", "precio_compra": 350000, "precio_venta": 420000, "stock": 3},
        {"nombre": "Volkswagen Golf 2023", "categoria": "Autos", "precio_compra": 470000, "precio_venta": 550000, "stock": 2},
        {"nombre": "Toyota RAV4 2023", "categoria": "SUV", "precio_compra": 600000, "precio_venta": 700000, "stock": 3},
        {"nombre": "Honda CR-V 2022", "categoria": "SUV", "precio_compra": 580000, "precio_venta": 680000, "stock": 4},
        {"nombre": "Hyundai Tucson 2023", "categoria": "SUV", "precio_compra": 550000, "precio_venta": 650000, "stock": 3},
        {"nombre": "Nissan Rogue 2022", "categoria": "SUV", "precio_compra": 540000, "precio_venta": 640000, "stock": 2},
        {"nombre": "Kia Sportage 2023", "categoria": "SUV", "precio_compra": 520000, "precio_venta": 620000, "stock": 3}
    ],
    "Ferretería": [
        {"nombre": "Cemento Gris Portland", "categoria": "Construcción", "precio_compra": 380, "precio_venta": 450, "stock": 200},
        {"nombre": "Varilla 3/8 Corrugada", "categoria": "Construcción", "precio_compra": 220, "precio_venta": 280, "stock": 500},
        {"nombre": "Pintura Tropical Base Agua 5G", "categoria": "Pinturas", "precio_compra": 1200, "precio_venta": 1500, "stock": 45},
        {"nombre": "Blocks 6\"", "categoria": "Construcción", "precio_compra": 45, "precio_venta": 60, "stock": 1000},
        {"nombre": "Plafón PVC Blanco", "categoria": "Techos", "precio_compra": 180, "precio_venta": 250, "stock": 300},
        {"nombre": "Juego Destornilladores Stanley", "categoria": "Herramientas", "precio_compra": 850, "precio_venta": 1100, "stock": 25},
        {"nombre": "Bombillos LED 9W", "categoria": "Eléctricos", "precio_compra": 95, "precio_venta": 140, "stock": 150},
        {"nombre": "Tomacorriente Cooper 110V", "categoria": "Eléctricos", "precio_compra": 120, "precio_venta": 180, "stock": 80},
        {"nombre": "Llave de Agua Plástica 1/2\"", "categoria": "Plomería", "precio_compra": 160, "precio_venta": 220, "stock": 60},
        {"nombre": "Cable THW #12 (metro)", "categoria": "Eléctricos", "precio_compra": 35, "precio_venta": 50, "stock": 1000},
        {"nombre": "Martillo Truper", "categoria": "Herramientas", "precio_compra": 340, "precio_venta": 450, "stock": 30},
        {"nombre": "Sierra Circular DeWalt", "categoria": "Herramientas Eléctricas", "precio_compra": 5800, "precio_venta": 7200, "stock": 8},
        {"nombre": "Tubo PVC 4\" (6m)", "categoria": "Plomería", "precio_compra": 420, "precio_venta": 580, "stock": 100},
        {"nombre": "Zinc Acanalado 6'", "categoria": "Techos", "precio_compra": 580, "precio_venta": 750, "stock": 150},
        {"nombre": "Cubeta Pintura Base Agua", "categoria": "Pinturas", "precio_compra": 2800, "precio_venta": 3500, "stock": 25}
    ],
    "Tienda Articulos Motos": [
            {"nombre": "Casco Integral DOT", "categoria": "Accesorios", "precio_compra": 2500, "precio_venta": 4000, "stock": 50},
            {"nombre": "Guantes de Moto Reforzados", "categoria": "Accesorios", "precio_compra": 800, "precio_venta": 1200, "stock": 100},
            {"nombre": "Cubre Asiento Antideslizante", "categoria": "Accesorios", "precio_compra": 300, "precio_venta": 600, "stock": 150},
            {"nombre": "Soporte para Teléfono", "categoria": "Accesorios", "precio_compra": 500, "precio_venta": 800, "stock": 120},
            {"nombre": "Chaleco Reflectante LED", "categoria": "Seguridad", "precio_compra": 900, "precio_venta": 1400, "stock": 75},
            {"nombre": "Luces LED para Moto", "categoria": "Iluminación", "precio_compra": 600, "precio_venta": 1000, "stock": 200},
            {"nombre": "Escape Deportivo", "categoria": "Repuestos", "precio_compra": 3500, "precio_venta": 5000, "stock": 30},
            {"nombre": "Espejos Retrovisores", "categoria": "Accesorios", "precio_compra": 300, "precio_venta": 600, "stock": 180},
            {"nombre": "Batería de Moto 12V", "categoria": "Componentes", "precio_compra": 1200, "precio_venta": 1800, "stock": 40},
            {"nombre": "Cargador USB para Moto", "categoria": "Accesorios", "precio_compra": 400, "precio_venta": 700, "stock": 100},
            {"nombre": "Pantalones de Protección", "categoria": "Vestimenta", "precio_compra": 1800, "precio_venta": 2600, "stock": 60},
            {"nombre": "Cámara de Llanta 17\"", "categoria": "Repuestos", "precio_compra": 500, "precio_venta": 800, "stock": 100},
            {"nombre": "Cadena y Piñón", "categoria": "Repuestos", "precio_compra": 900, "precio_venta": 1400, "stock": 50},
            {"nombre": "Impermeable para Moto", "categoria": "Vestimenta", "precio_compra": 700, "precio_venta": 1200, "stock": 80},
            {"nombre": "Frenos de Disco", "categoria": "Repuestos", "precio_compra": 1500, "precio_venta": 2200, "stock": 40},
            {"nombre": "Kit de Herramientas", "categoria": "Accesorios", "precio_compra": 600, "precio_venta": 1000, "stock": 70},
            {"nombre": "Aceite para Motor 10W40", "categoria": "Lubricantes", "precio_compra": 400, "precio_venta": 700, "stock": 120},
            {"nombre": "Filtro de Aire", "categoria": "Repuestos", "precio_compra": 300, "precio_venta": 500, "stock": 100},
            {"nombre": "Cubre Manos", "categoria": "Accesorios", "precio_compra": 200, "precio_venta": 400, "stock": 150},
            {"nombre": "Casco Abierto", "categoria": "Accesorios", "precio_compra": 1800, "precio_venta": 2500, "stock": 40},
            {"nombre": "Pastillas de Freno", "categoria": "Repuestos", "precio_compra": 500, "precio_venta": 800, "stock": 90},
            {"nombre": "Antirrobo para Moto", "categoria": "Seguridad", "precio_compra": 700, "precio_venta": 1200, "stock": 70},
            {"nombre": "Protección de Tanque", "categoria": "Accesorios", "precio_compra": 300, "precio_venta": 600, "stock": 80},
            {"nombre": "Maletero para Moto", "categoria": "Accesorios", "precio_compra": 2500, "precio_venta": 4000, "stock": 30},
            {"nombre": "Pito Eléctrico", "categoria": "Componentes", "precio_compra": 200, "precio_venta": 400, "stock": 200}
        ],
    "Tienda de Ropa de Marca": [
            {"nombre": "Camiseta Polo Ralph Lauren", "categoria": "Camisetas", "precio_compra": 2500, "precio_venta": 4000, "stock": 50},
            {"nombre": "Pantalón Chino Dockers", "categoria": "Pantalones", "precio_compra": 3500, "precio_venta": 5000, "stock": 40},
            {"nombre": "Vestido Zara", "categoria": "Vestidos", "precio_compra": 4500, "precio_venta": 7000, "stock": 30},
            {"nombre": "Jeans Levi's 501", "categoria": "Jeans", "precio_compra": 4000, "precio_venta": 6000, "stock": 60},
            {"nombre": "Chaqueta de Cuero Guess", "categoria": "Chaquetas", "precio_compra": 8000, "precio_venta": 12000, "stock": 20},
            {"nombre": "Camiseta Nike Dri-Fit", "categoria": "Camisetas", "precio_compra": 1800, "precio_venta": 3000, "stock": 80},
            {"nombre": "Sudadera Adidas Originals", "categoria": "Sudaderas", "precio_compra": 3000, "precio_venta": 4500, "stock": 50},
            {"nombre": "Traje Hugo Boss", "categoria": "Trajes", "precio_compra": 15000, "precio_venta": 20000, "stock": 15},
            {"nombre": "Falda Mango", "categoria": "Faldas", "precio_compra": 2500, "precio_venta": 3800, "stock": 40},
            {"nombre": "Camisa Formal Tommy Hilfiger", "categoria": "Camisas", "precio_compra": 3000, "precio_venta": 5000, "stock": 30},
            {"nombre": "Blusa H&M", "categoria": "Blusas", "precio_compra": 1200, "precio_venta": 2000, "stock": 80},
            {"nombre": "Short Calvin Klein", "categoria": "Shorts", "precio_compra": 2000, "precio_venta": 3500, "stock": 50},
            {"nombre": "Abrigo Burberry", "categoria": "Abrigos", "precio_compra": 20000, "precio_venta": 28000, "stock": 10},
            {"nombre": "Polo Lacoste", "categoria": "Polos", "precio_compra": 4000, "precio_venta": 6000, "stock": 40},
            {"nombre": "Pantalón Deportivo Puma", "categoria": "Pantalones", "precio_compra": 1800, "precio_venta": 2800, "stock": 60},
            {"nombre": "Chamarra Levi's", "categoria": "Chaquetas", "precio_compra": 4500, "precio_venta": 6500, "stock": 25},
            {"nombre": "Mono Deportivo Nike", "categoria": "Monos", "precio_compra": 3500, "precio_venta": 5000, "stock": 30},
            {"nombre": "Cardigan Zara", "categoria": "Suéteres", "precio_compra": 2500, "precio_venta": 4000, "stock": 40},
            {"nombre": "Jeans Skinny Fit Levi's", "categoria": "Jeans", "precio_compra": 4200, "precio_venta": 6500, "stock": 50},
            {"nombre": "Blazer Massimo Dutti", "categoria": "Blazers", "precio_compra": 6000, "precio_venta": 9000, "stock": 15},
            {"nombre": "Leggings Gymshark", "categoria": "Leggings", "precio_compra": 1500, "precio_venta": 2500, "stock": 100},
            {"nombre": "Camisa Casual Springfield", "categoria": "Camisas", "precio_compra": 2500, "precio_venta": 4000, "stock": 50},
            {"nombre": "Vestido Corto Bershka", "categoria": "Vestidos", "precio_compra": 2000, "precio_venta": 3500, "stock": 60},
            {"nombre": "Chaleco North Face", "categoria": "Chalecos", "precio_compra": 6000, "precio_venta": 8500, "stock": 20},
            {"nombre": "Top Crop Forever 21", "categoria": "Tops", "precio_compra": 1200, "precio_venta": 2000, "stock": 90},
            {"nombre": "Falda Midi Stradivarius", "categoria": "Faldas", "precio_compra": 1800, "precio_venta": 3000, "stock": 50},
            {"nombre": "Bikini Victoria's Secret", "categoria": "Trajes de baño", "precio_compra": 2200, "precio_venta": 3500, "stock": 40},
            {"nombre": "Overol GAP", "categoria": "Overoles", "precio_compra": 3000, "precio_venta": 4800, "stock": 20},
            {"nombre": "Suéter Columbia", "categoria": "Suéteres", "precio_compra": 2800, "precio_venta": 4000, "stock": 30},
            {"nombre": "Chamarra Deportiva Adidas", "categoria": "Chaquetas", "precio_compra": 4000, "precio_venta": 6000, "stock": 25},
            {"nombre": "Camiseta Estampada Uniqlo", "categoria": "Camisetas", "precio_compra": 1200, "precio_venta": 2000, "stock": 100},
            {"nombre": "Traje de Baño Speedo", "categoria": "Trajes de baño", "precio_compra": 2500, "precio_venta": 4000, "stock": 40},
            {"nombre": "Short Denim Levi's", "categoria": "Shorts", "precio_compra": 2200, "precio_venta": 3500, "stock": 30},
            {"nombre": "Abrigo Largo Mango", "categoria": "Abrigos", "precio_compra": 15000, "precio_venta": 20000, "stock": 15},
            {"nombre": "Camiseta Básica H&M", "categoria": "Camisetas", "precio_compra": 800, "precio_venta": 1500, "stock": 120},
            {"nombre": "Camisa Formal Massimo Dutti", "categoria": "Camisas", "precio_compra": 3500, "precio_venta": 5000, "stock": 40},
            {"nombre": "Vestido Largo Guess", "categoria": "Vestidos", "precio_compra": 6000, "precio_venta": 9000, "stock": 20},
            {"nombre": "Falda Plisada Zara", "categoria": "Faldas", "precio_compra": 2000, "precio_venta": 3500, "stock": 50},
            {"nombre": "Leggings Adidas", "categoria": "Leggings", "precio_compra": 1800, "precio_venta": 3000, "stock": 70},
            {"nombre": "Cárdigan H&M", "categoria": "Suéteres", "precio_compra": 1500, "precio_venta": 2500, "stock": 40},
            {"nombre": "Parka Timberland", "categoria": "Chaquetas", "precio_compra": 8000, "precio_venta": 12000, "stock": 10},
            {"nombre": "Traje Completo Zara", "categoria": "Trajes", "precio_compra": 10000, "precio_venta": 15000, "stock": 10},
            {"nombre": "Camisa de Lino Springfield", "categoria": "Camisas", "precio_compra": 3000, "precio_venta": 4500, "stock": 30},
            {"nombre": "Bermudas Pull&Bear", "categoria": "Shorts", "precio_compra": 1500, "precio_venta": 2500, "stock": 60},
            {"nombre": "Mono Largo H&M", "categoria": "Monos", "precio_compra": 3500, "precio_venta": 5000, "stock": 25},
            {"nombre": "Pantalón Jogger Puma", "categoria": "Pantalones", "precio_compra": 2000, "precio_venta": 3500, "stock": 40},
            {"nombre": "Blusa Zara", "categoria": "Blusas", "precio_compra": 1800, "precio_venta": 3000, "stock": 70},
    ],
    "Liquor Store": [
            {"nombre": "Brugal Extra Viejo", "categoria": "Ron", "marca": "Brugal", "precio_compra": 800, "precio_venta": 1200, "stock": 50},
            {"nombre": "Barceló Imperial", "categoria": "Ron", "marca": "Barceló", "precio_compra": 1200, "precio_venta": 1700, "stock": 40},
            {"nombre": "Ron Matusalem Gran Reserva", "categoria": "Ron", "marca": "Matusalem", "precio_compra": 1000, "precio_venta": 1500, "stock": 45},
            {"nombre": "Bacardi 8 Años", "categoria": "Ron", "marca": "Bacardi", "precio_compra": 1400, "precio_venta": 2000, "stock": 35},
            {"nombre": "Ron La Fortaleza", "categoria": "Ron", "marca": "La Fortaleza", "precio_compra": 1100, "precio_venta": 1600, "stock": 30},
            {"nombre": "Brugal 1888", "categoria": "Ron", "marca": "Brugal", "precio_compra": 2500, "precio_venta": 3500, "stock": 20},
            {"nombre": "Ron Clásico Barcelo", "categoria": "Ron", "marca": "Barceló", "precio_compra": 600, "precio_venta": 1000, "stock": 70},
            {"nombre": "Ron Presidente", "categoria": "Ron", "marca": "Presidente", "precio_compra": 400, "precio_venta": 700, "stock": 100},
            {"nombre": "Santo Domingo Ron", "categoria": "Ron", "marca": "Santo Domingo", "precio_compra": 350, "precio_venta": 600, "stock": 90},
            {"nombre": "Mango Bay Rum", "categoria": "Ron", "marca": "Mango Bay", "precio_compra": 1200, "precio_venta": 1700, "stock": 50},
            {"nombre": "Cerveza Presidente", "categoria": "Cerveza", "marca": "Presidente", "precio_compra": 80, "precio_venta": 150, "stock": 200},
            {"nombre": "Cerveza Brahma Light", "categoria": "Cerveza", "marca": "Brahma", "precio_compra": 70, "precio_venta": 120, "stock": 180},
            {"nombre": "Cerveza Red Stripe", "categoria": "Cerveza", "marca": "Red Stripe", "precio_compra": 90, "precio_venta": 140, "stock": 160},
            {"nombre": "Cerveza Presidente Light", "categoria": "Cerveza", "marca": "Presidente", "precio_compra": 85, "precio_venta": 130, "stock": 170},
            {"nombre": "Vino Sangría Don Simon", "categoria": "Vino", "marca": "Don Simon", "precio_compra": 400, "precio_venta": 650, "stock": 60},
            {"nombre": "Vino Tinto Lancers", "categoria": "Vino", "marca": "Lancers", "precio_compra": 600, "precio_venta": 900, "stock": 50},
            {"nombre": "Vino Blanco Sutter Home", "categoria": "Vino", "marca": "Sutter Home", "precio_compra": 800, "precio_venta": 1200, "stock": 30},
            {"nombre": "Vino Dominicano Vino del Sol", "categoria": "Vino", "marca": "Vino del Sol", "precio_compra": 700, "precio_venta": 1000, "stock": 40},
            {"nombre": "Tequila José Cuervo", "categoria": "Tequila", "marca": "José Cuervo", "precio_compra": 1200, "precio_venta": 1700, "stock": 20},
            {"nombre": "Tequila Don Julio 1942", "categoria": "Tequila", "marca": "Don Julio", "precio_compra": 3000, "precio_venta": 4500, "stock": 10},
            {"nombre": "Tequila El Jimador", "categoria": "Tequila", "marca": "El Jimador", "precio_compra": 1500, "precio_venta": 2200, "stock": 25},
            {"nombre": "Gin Tanqueray", "categoria": "Ginebra", "marca": "Tanqueray", "precio_compra": 1800, "precio_venta": 2600, "stock": 30},
            {"nombre": "Gin Beefeater", "categoria": "Ginebra", "marca": "Beefeater", "precio_compra": 1500, "precio_venta": 2200, "stock": 40},
            {"nombre": "Vodka Absolut", "categoria": "Vodka", "marca": "Absolut", "precio_compra": 1200, "precio_venta": 1800, "stock": 35},
            {"nombre": "Vodka Smirnoff", "categoria": "Vodka", "marca": "Smirnoff", "precio_compra": 1000, "precio_venta": 1500, "stock": 50},
            {"nombre": "Whisky Johnnie Walker Black", "categoria": "Whisky", "marca": "Johnnie Walker", "precio_compra": 2000, "precio_venta": 3000, "stock": 30},
            {"nombre": "Whisky Macallan 12 Años", "categoria": "Whisky", "marca": "Macallan", "precio_compra": 5000, "precio_venta": 7500, "stock": 10},
            {"nombre": "Whisky Chivas Regal 12", "categoria": "Whisky", "marca": "Chivas Regal", "precio_compra": 2500, "precio_venta": 3500, "stock": 25},
            {"nombre": "Whisky Glenfiddich 18", "categoria": "Whisky", "marca": "Glenfiddich", "precio_compra": 4500, "precio_venta": 6500, "stock": 15},
            {"nombre": "Vino Dominicano Casa de Campo", "categoria": "Vino", "marca": "Casa de Campo", "precio_compra": 1000, "precio_venta": 1500, "stock": 40},
            {"nombre": "Mojito Ron Matusalem", "categoria": "Cócteles", "marca": "Matusalem", "precio_compra": 1500, "precio_venta": 2200, "stock": 30},
            {"nombre": "Coñac Hennessy VS", "categoria": "Coñac", "marca": "Hennessy", "precio_compra": 2500, "precio_venta": 3500, "stock": 20},
            {"nombre": "Coñac Rémy Martin VSOP", "categoria": "Coñac", "marca": "Rémy Martin", "precio_compra": 3000, "precio_venta": 4500, "stock": 15},
            {"nombre": "Pina Colada Presidente", "categoria": "Cócteles", "marca": "Presidente", "precio_compra": 1800, "precio_venta": 2600, "stock": 25},
            {"nombre": "Aguardiente La Caña", "categoria": "Aguardiente", "marca": "La Caña", "precio_compra": 700, "precio_venta": 1000, "stock": 60},
            {"nombre": "Ron Quorhum 30", "categoria": "Ron", "marca": "Quorhum", "precio_compra": 2000, "precio_venta": 3000, "stock": 20},
            {"nombre": "Ron Blanco Barcelo", "categoria": "Ron", "marca": "Barceló", "precio_compra": 600, "precio_venta": 900, "stock": 70},
            {"nombre": "Vino Moscato Stella Rosa", "categoria": "Vino", "marca": "Stella Rosa", "precio_compra": 1200, "precio_venta": 1800, "stock": 40},
            {"nombre": "Vino Espumante Dom Perignon", "categoria": "Vino", "marca": "Dom Perignon", "precio_compra": 8000, "precio_venta": 12000, "stock": 5},
            {"nombre": "Cerveza Presidente Dorada", "categoria": "Cerveza", "marca": "Presidente", "precio_compra": 90, "precio_venta": 140, "stock": 150},
            {"nombre": "Cerveza Ambar", "categoria": "Cerveza", "marca": "Ambar", "precio_compra": 120, "precio_venta": 180, "stock": 110},
            {"nombre": "Cerveza Corona", "categoria": "Cerveza", "marca": "Corona", "precio_compra": 110, "precio_venta": 160, "stock": 130},
            {"nombre": "Vino Tinto Concha y Toro", "categoria": "Vino", "marca": "Concha y Toro", "precio_compra": 800, "precio_venta": 1200, "stock": 60},
            {"nombre": "Aguardiente Anis", "categoria": "Aguardiente", "marca": "Anis", "precio_compra": 400, "precio_venta": 600, "stock": 90},
            {"nombre": "Limoncello Italiano", "categoria": "Licores", "marca": "Limoncello", "precio_compra": 2000, "precio_venta": 2900, "stock": 15},
            {"nombre": "Vino Blanco Santa Carolina", "categoria": "Vino", "marca": "Santa Carolina", "precio_compra": 900, "precio_venta": 1400, "stock": 50},
            {"nombre": "Tequila Espolon Blanco", "categoria": "Tequila", "marca": "Espolon", "precio_compra": 1000, "precio_venta": 1500, "stock": 45},
            {"nombre": "Johnnie Walker Red Label", "categoria": "Whisky", "marca": "Johnnie Walker", "precio_compra": 1000, "precio_venta": 1500, "stock": 40},
            {"nombre": "Johnnie Walker Black Label", "categoria": "Whisky", "marca": "Johnnie Walker", "precio_compra": 2000, "precio_venta": 3000, "stock": 30},
            {"nombre": "Chivas Regal 12 Años", "categoria": "Whisky", "marca": "Chivas Regal", "precio_compra": 1500, "precio_venta": 2200, "stock": 35},
            {"nombre": "Jameson Irish Whiskey", "categoria": "Whisky", "marca": "Jameson", "precio_compra": 1400, "precio_venta": 2000, "stock": 50},
            {"nombre": "Glenfiddich 12 Años", "categoria": "Whisky", "marca": "Glenfiddich", "precio_compra": 2500, "precio_venta": 3500, "stock": 25},
            {"nombre": "Macallan 12 Años", "categoria": "Whisky", "marca": "Macallan", "precio_compra": 4500, "precio_venta": 6500, "stock": 20},
            {"nombre": "Ballantine's Finest", "categoria": "Whisky", "marca": "Ballantine's", "precio_compra": 1200, "precio_venta": 1700, "stock": 60},
            {"nombre": "Aberlour 12 Años", "categoria": "Whisky", "marca": "Aberlour", "precio_compra": 3500, "precio_venta": 5000, "stock": 15},
            {"nombre": "The Glenlivet 12 Años", "categoria": "Whisky", "marca": "The Glenlivet", "precio_compra": 2800, "precio_venta": 4000, "stock": 30},
            {"nombre": "Bushmills Original", "categoria": "Whisky", "marca": "Bushmills", "precio_compra": 1300, "precio_venta": 1800, "stock": 50},
            {"nombre": "Dewar's White Label", "categoria": "Whisky", "marca": "Dewar's", "precio_compra": 1000, "precio_venta": 1500, "stock": 70},
            {"nombre": "Royal Salute 21 Años", "categoria": "Whisky", "marca": "Royal Salute", "precio_compra": 8000, "precio_venta": 12000, "stock": 10},
            {"nombre": "Glenmorangie Original 10 Años", "categoria": "Whisky", "marca": "Glenmorangie", "precio_compra": 3500, "precio_venta": 5000, "stock": 15},
            {"nombre": "Red Label Johnnie Walker", "categoria": "Whisky", "marca": "Johnnie Walker", "precio_compra": 1100, "precio_venta": 1600, "stock": 40},
            {"nombre": "Ardbeg 10 Años", "categoria": "Whisky", "marca": "Ardbeg", "precio_compra": 4000, "precio_venta": 6000, "stock": 10},
             {"nombre": "Vino Tinto Concha y Toro", "categoria": "Vino Tinto", "marca": "Concha y Toro", "precio_compra": 800, "precio_venta": 1200, "stock": 60},
            {"nombre": "Vino Blanco Santa Carolina", "categoria": "Vino Blanco", "marca": "Santa Carolina", "precio_compra": 900, "precio_venta": 1400, "stock": 50},
            {"nombre": "Vino Tinto Casillero del Diablo", "categoria": "Vino Tinto", "marca": "Casillero del Diablo", "precio_compra": 850, "precio_venta": 1300, "stock": 55},
            {"nombre": "Vino Rosado Santa Rita 120", "categoria": "Vino Rosado", "marca": "Santa Rita", "precio_compra": 700, "precio_venta": 1100, "stock": 45},
            {"nombre": "Vino Tinto Marqués de Riscal", "categoria": "Vino Tinto", "marca": "Marqués de Riscal", "precio_compra": 1500, "precio_venta": 2200, "stock": 30},
            {"nombre": "Vino Blanco Torres", "categoria": "Vino Blanco", "marca": "Torres", "precio_compra": 950, "precio_venta": 1400, "stock": 60},
            {"nombre": "Vino Tinto Robert Mondavi", "categoria": "Vino Tinto", "marca": "Robert Mondavi", "precio_compra": 1800, "precio_venta": 2500, "stock": 40},
            {"nombre": "Vino Tinto Bodega Norton Reserva", "categoria": "Vino Tinto", "marca": "Bodega Norton", "precio_compra": 1200, "precio_venta": 1800, "stock": 50},
            {"nombre": "Vino Tinto La Caña", "categoria": "Vino Tinto", "marca": "La Caña", "precio_compra": 600, "precio_venta": 1000, "stock": 70},
            {"nombre": "Vino Dominicano Viticultura La Penda", "categoria": "Vino Tinto", "marca": "Viticultura La Penda", "precio_compra": 1500, "precio_venta": 2300, "stock": 25}
        ],
        "Tienda de Calzados": [
            {"nombre": "Nike Air Max 90", "categoria": "Tenis/Hombre", "tipo": "Deportivo", "genero": "Hombre", "marca": "Nike", "precio_compra": 3000, "precio_venta": 4500, "stock": 80},
            {"nombre": "Adidas Ultraboost 22", "categoria": "Tenis/Hombre", "tipo": "Deportivo", "genero": "Hombre", "marca": "Adidas", "precio_compra": 3500, "precio_venta": 5000, "stock": 70},
            {"nombre": "Converse Chuck Taylor All Star", "categoria": "Zapatillas/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "Converse", "precio_compra": 2000, "precio_venta": 3000, "stock": 100},
            {"nombre": "Vans Old Skool", "categoria": "Zapatillas/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "Vans", "precio_compra": 2500, "precio_venta": 3700, "stock": 90},
            {"nombre": "Reebok Classic Leather", "categoria": "Zapatillas/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "Reebok", "precio_compra": 2200, "precio_venta": 3400, "stock": 85},
            {"nombre": "Puma RS-X", "categoria": "Tenis/Hombre", "tipo": "Deportivo", "genero": "Hombre", "marca": "Puma", "precio_compra": 3000, "precio_venta": 4500, "stock": 60},
            {"nombre": "Dr. Martens 1460", "categoria": "Botas/Unisex", "tipo": "Clásico", "genero": "Unisex", "marca": "Dr. Martens", "precio_compra": 5000, "precio_venta": 7000, "stock": 40},
            {"nombre": "Timberland Premium Waterproof Boots", "categoria": "Botas/Hombre", "tipo": "Casual", "genero": "Hombre", "marca": "Timberland", "precio_compra": 4800, "precio_venta": 6500, "stock": 50},
            {"nombre": "Clarks Desert Boots", "categoria": "Botas/Hombre", "tipo": "Casual", "genero": "Hombre", "marca": "Clarks", "precio_compra": 3000, "precio_venta": 4500, "stock": 60},
            {"nombre": "Nike Dunk Low", "categoria": "Tenis/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "Nike", "precio_compra": 3500, "precio_venta": 5000, "stock": 75},
            {"nombre": "Adidas Gazelle", "categoria": "Zapatillas/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "Adidas", "precio_compra": 2500, "precio_venta": 4000, "stock": 90},
            {"nombre": "Asics Gel-Kayano 28", "categoria": "Tenis/Hombre", "tipo": "Deportivo", "genero": "Hombre", "marca": "Asics", "precio_compra": 3200, "precio_venta": 4800, "stock": 65},
            {"nombre": "Hoka Clifton 9", "categoria": "Tenis/Hombre", "tipo": "Deportivo", "genero": "Hombre", "marca": "Hoka", "precio_compra": 4000, "precio_venta": 6000, "stock": 50},
            {"nombre": "New Balance 574", "categoria": "Zapatillas/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "New Balance", "precio_compra": 2600, "precio_venta": 3900, "stock": 80},
            {"nombre": "Gucci Ace Sneakers", "categoria": "Tenis de Lujo/Unisex", "tipo": "De Vestir", "genero": "Unisex", "marca": "Gucci", "precio_compra": 12000, "precio_venta": 18000, "stock": 20},
            {"nombre": "Balenciaga Triple S", "categoria": "Tenis de Lujo/Unisex", "tipo": "Deportivo", "genero": "Unisex", "marca": "Balenciaga", "precio_compra": 14000, "precio_venta": 21000, "stock": 15},
            {"nombre": "Christian Louboutin So Kate", "categoria": "Tacos/Mujer", "tipo": "De Vestir", "genero": "Mujer", "marca": "Christian Louboutin", "precio_compra": 8000, "precio_venta": 12000, "stock": 25},
            {"nombre": "Jimmy Choo Romy 100", "categoria": "Tacos/Mujer", "tipo": "De Vestir", "genero": "Mujer", "marca": "Jimmy Choo", "precio_compra": 7000, "precio_venta": 11000, "stock": 30},
            {"nombre": "Steve Madden Carrson", "categoria": "Tacos/Mujer", "tipo": "Casual", "genero": "Mujer", "marca": "Steve Madden", "precio_compra": 3500, "precio_venta": 5000, "stock": 40},
            {"nombre": "Crocs Classic Clog", "categoria": "Sandalias/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "Crocs", "precio_compra": 1500, "precio_venta": 2200, "stock": 100},
            {"nombre": "Birkenstock Arizona", "categoria": "Sandalias/Unisex", "tipo": "Casual", "genero": "Unisex", "marca": "Birkenstock", "precio_compra": 1800, "precio_venta": 2700, "stock": 80},
            {"nombre": "Tory Burch Miller Sandal", "categoria": "Sandalias/Mujer", "tipo": "Casual", "genero": "Mujer", "marca": "Tory Burch", "precio_compra": 4000, "precio_venta": 6000, "stock": 35},
            {"nombre": "Cole Haan GrandPro Tennis", "categoria": "Tenis/Hombre", "tipo": "Casual", "genero": "Hombre", "marca": "Cole Haan", "precio_compra": 3200, "precio_venta": 4800, "stock": 45},
            {"nombre": "Aldo Men's Dress Shoes", "categoria": "Zapatos Formales/Hombre", "tipo": "De Vestir", "genero": "Hombre", "marca": "Aldo", "precio_compra": 3000, "precio_venta": 4500, "stock": 40},
            {"nombre": "Salvatore Ferragamo Oxford", "categoria": "Zapatos Formales/Hombre", "tipo": "De Vestir", "genero": "Hombre", "marca": "Salvatore Ferragamo", "precio_compra": 9000, "precio_venta": 13500, "stock": 20},
            {"nombre": "Allen Edmonds Park Avenue", "categoria": "Zapatos Formales/Hombre", "tipo": "De Vestir", "genero": "Hombre", "marca": "Allen Edmonds", "precio_compra": 6000, "precio_venta": 9000, "stock": 30},
            {"nombre": "Nike ZoomX Vaporfly", "categoria": "Tenis/Hombre", "tipo": "Deportivo", "genero": "Hombre", "marca": "Nike", "precio_compra": 4500, "precio_venta": 7000, "stock": 40},
            {"nombre": "Saucony Endorphin Speed 3", "categoria": "Tenis/Unisex", "tipo": "Deportivo", "genero": "Unisex", "marca": "Saucony", "precio_compra": 4000, "precio_venta": 6000, "stock": 50},
            {"nombre": "Clarks Women's Pump", "categoria": "Tacos/Mujer", "tipo": "De Vestir", "genero": "Mujer", "marca": "Clarks", "precio_compra": 3500, "precio_venta": 5000, "stock": 60}
        ]



   
}

# Función para generar clientes y vendedores
def generar_entidades(cantidad, regiones, tipo):
    nombres_base = {
        "cliente": [
            "Juan Pérez", "María Gómez", "Pedro Rodríguez", "Ana Martínez", "Luis Fernández",
            "Carlos Ramírez", "Rosa Vargas", "Manuel Castillo", "Carmen Reyes", "David Núñez",
            "Paola Batista", "Javier López", "Natalia Cabrera", "Andrés Cruz", "Marta Hidalgo",
            "Ricardo Aquino", "Lorena Santana", "Diego Rosario", "Julia Espinal", "Santiago Guzmán",
            "Gabriela Domínguez", "Fernando Morales", "Isabel Rivera", "Alejandro Suárez", "Patricia Salazar",
            "Sofía Ortega", "Mario Jiménez", "Valeria Mendoza", "Francisco Solano", "Claudia Villalobos",
            "Héctor López", "Teresa Gutiérrez", "Jorge Escobar", "Camila Vega", "Roberto Almonte",
            "Laura Herrera", "Daniela Peña", "Miguel Cabrera", "Andrea Torres", "Adriana Paredes",
            "Enrique Montalvo", "Vanessa Ortiz", "Lucía Montes", "Pablo Rojas", "Cristina Navarro",
            "Esteban Méndez", "Liliana Sánchez", "Emilio Vargas", "Alejandra Serrano", "Ángel Carrillo"
        ]        ,
        "vendedor": [
            "Carla Santos", "José Jiménez", "Laura Díaz", "Francisco Peña", "Sofía Castillo",
            "Miguel Almonte", "Gabriela Torres", "Raúl Méndez", "Lucía Vargas", "Fernando Guerrero",
            "Liliana Pérez", "Jorge Sánchez", "Esther Molina", "Ángel Rosario", "Valeria De la Cruz",
            "Víctor Morales", "Claudia Paredes", "Sebastián Ramos", "Daniela Suárez", "Felipe Medina"
        ],
        
    }

    return [
        {"nombre": f"{random.choice(nombres_base[tipo])} {i+1}", "region": random.choice(regiones)}
        for i in range(cantidad)
    ]

# Función modificada para generar productos solo del tipo de negocio seleccionado
def generar_productos(cantidad, tipo_negocio):
    # Obtener solo los productos del tipo de negocio seleccionado
    productos_disponibles = productos_base[tipo_negocio]
    # Generar lista de productos con copias profundas para no modificar los originales
    productos_seleccionados = []
    
    for _ in range(cantidad):
        # Seleccionar un producto aleatorio y crear una copia de sus datos
        producto_original = random.choice(productos_disponibles)
        producto_copia = {
            "nombre": producto_original["nombre"],
            "categoria": producto_original["categoria"],
            "precio_compra": producto_original["precio_compra"],
            "precio_venta": producto_original["precio_venta"],
            "stock": producto_original["stock"]
        }
        productos_seleccionados.append(producto_copia)
    
    return productos_seleccionados


# Función para generar datos de ventas
def generar_datos_ventas(fecha_inicio, fecha_final, num_facturas, clientes, vendedores, productos):
    tipo_pago = ["Crédito", "Efectivo", "Transferencia"]
    tipo_compra = ["Física", "Envío"]
    datos_ventas = []

    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_final = datetime.strptime(fecha_final, "%Y-%m-%d")
    delta = fecha_final - fecha_inicio

    # ID único para cada venta
    id_counter = 1

    for factura_id in range(1, num_facturas + 1):
        cliente = random.choice(clientes)
        region = cliente["region"]

        # Filtrar vendedores por la misma región que el cliente
        vendedores_en_region = [v for v in vendedores if v["region"] == region]
        if not vendedores_en_region:
            continue

        vendedor = random.choice(vendedores_en_region)
        num_productos = random.randint(1, 5)
        fecha = fecha_inicio + timedelta(days=random.randint(0, delta.days))
        tipo_pago_seleccionado = random.choice(tipo_pago)
        tipo_compra_seleccionado = random.choice(tipo_compra)

        for _ in range(num_productos):
            producto = random.choice(productos)
            cantidad = random.randint(1, 10)

            # Asegurar que la cantidad no exceda el stock disponible
            if producto["stock"] > 0:  # Solo procesar si hay stock disponible
                cantidad = min(cantidad, producto["stock"])
                stock_actual = producto["stock"] - cantidad
                producto["stock"] = stock_actual

                subtotal = cantidad * producto["precio_venta"]
                itbis = round(subtotal * 0.18, 2)
                total = subtotal + itbis

                # Cálculos adicionales
                costo = cantidad * producto["precio_compra"]  # Costo = Cantidad * Precio de Compra
                margen = total - costo  # Margen = Total - Costo
               # Calculando porcentaje de margen como un valor decimal
                porcentaje_margen = (margen / total) if total > 0 else 0  
                
                # Generar un ID único para cada fila
                id_unico = id_counter
                id_counter += 1

                datos_ventas.append({
                    "ID": id_unico,  # Agregar la columna ID
                    "FECHA": fecha.strftime("%Y-%m-%d"),
                    "FACTURA": factura_id,
                    "REGION": region,
                    "CLIENTE": cliente["nombre"],
                    "TIPO_PAGO": tipo_pago_seleccionado,
                    "VENDEDOR": vendedor["nombre"],
                    "TIPO_COMPRA": tipo_compra_seleccionado,
                    "PRODUCTO": producto["nombre"],
                    "CATEGORIA": producto["categoria"],
                    "EXISTENCIA": producto["stock"] + cantidad,
                    "PRECIO_COMPRA": producto["precio_compra"],
                    "PRECIO_VENTAS": producto["precio_venta"],
                    "CANTIDAD": cantidad,
                    "SUBTOTAL": subtotal,
                    "ITBIS": itbis,
                    "TOTAL": total,
                    "STOCK": stock_actual,
                    "COSTO": costo,
                    "MARGEN": margen,
                    "% MARGEN": round(porcentaje_margen, 2)
                })

    return pd.DataFrame(datos_ventas)

# Interfaz en Streamlit
st.markdown(
    """
    <h2 style='text-align: center;'>📊 Generador de Datos de Ventas 📊</h2>
    """,
    unsafe_allow_html=True,
)

# Selección de tipo de negocio
tipo_negocio = st.selectbox("Selecciona el tipo de negocio", list(productos_base.keys()))

# Parámetros para clientes, vendedores, productos
num_clientes = st.number_input("Cantidad de clientes", min_value=1, max_value=50, value=25)
num_vendedores = st.number_input("Cantidad de vendedores", min_value=1, max_value=25, value=15)
num_productos = st.number_input("Cantidad de productos", min_value=1, max_value=50, value=25)

# Parámetros adicionales
fecha_inicio = st.date_input("Fecha de inicio", value=datetime(2020, 1, 1))
fecha_final = st.date_input("Fecha final", value=datetime(2024, 12, 31))
num_facturas = st.number_input("Cantidad de facturas", min_value=1, max_value=10000,value=100)

# Botones para generar y guardar datos
if st.button("Generar Datos"):
    regiones = ["Norte", "Sur", "Este", "Oeste"]
    clientes = generar_entidades(num_clientes, regiones, "cliente")
    vendedores = generar_entidades(num_vendedores, regiones, "vendedor")
    productos = generar_productos(num_productos, tipo_negocio)  # Modificado para pasar tipo_negocio

    ventas_df = generar_datos_ventas(
        fecha_inicio.strftime("%Y-%m-%d"),
        fecha_final.strftime("%Y-%m-%d"),
        int(num_facturas),
        clientes,
        vendedores,
        productos,
    )

    st.success(f"Datos generados correctamente para {tipo_negocio}")
    st.dataframe(ventas_df)

    # Almacenar en el estado para guardar luego
    st.session_state["ventas_df"] = ventas_df

# Campo para nombre de archivo
nombre_archivo = st.text_input("Nombre del archivo de salida", "datos_ventas.xlsx")

# Botón para guardar el archivo
if st.button("Guardar Datos"):
    if "ventas_df" in st.session_state:
        ventas_df = st.session_state["ventas_df"]

        try:
            # Crear la carpeta si no existe
            output_dir = "descargas"  # Carpeta de destino
            os.makedirs(output_dir, exist_ok=True)
            file_path = os.path.join(output_dir, nombre_archivo)

            # Eliminar el índice antes de exportar
            ventas_df_reset = ventas_df.reset_index(drop=True)  # Eliminar el índice automáticamente creado por pandas

            # Guardar el archivo en la carpeta
            with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
                ventas_df_reset.to_excel(writer, index=False, sheet_name="Ventas")

            st.success(f"Archivo guardado en: {file_path}")

            # Descargar el archivo
            with open(file_path, "rb") as f:
                st.download_button(
                    label="Descargar archivo",
                    data=f,
                    file_name=nombre_archivo,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

        except Exception as e:
            st.error(f"Error al guardar el archivo: {e}")
    else:
        st.warning("Primero genera los datos antes de intentar guardarlos.")
