<!DOCTYPE html>
<html>
<head>
    <title>Sales Data Analysis Report</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f5f7fa;
            color: #222;
        }

        h1 {
            color: #1f4e79;
        }

        h2 {
            color: #2f75b5;
            margin-top: 30px;
        }

        .card {
            background-color: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        ul {
            line-height: 1.8;
        }

        img {
            max-width: 700px;
            width: 100%;
            display: block;
            margin: 20px 0;
            border: 1px solid #ddd;
            border-radius: 8px;
            background-color: white;
        }
    </style>
</head>
<body>

    <h1>Sales Data Analysis Report</h1>

    <div class="card">
        <h2>Project Objective</h2>
        <p>
            This project analyzes sales data using Python, pandas, and matplotlib.
            The goal is to find total revenue, best product, best category,
            best city, and top customer.
        </p>
    </div>

    <div class="card">
        <h2>Key Results</h2>
        <ul>
            <li>Total revenue: 2865</li>
            <li>Best product: Laptop with revenue 1600</li>
            <li>Best category: Electronics with revenue 1875</li>
            <li>Best city: Chicago with revenue 1250</li>
            <li>Top customer: Alice with spending 1175</li>
        </ul>
    </div>

    <div class="card">
        <h2>Simple Insights</h2>
        <ul>
            <li>Laptop generated the highest revenue among all products.</li>
            <li>Electronics performed better than Furniture.</li>
            <li>Chicago generated the highest revenue among all cities.</li>
            <li>Alice is the highest-spending customer.</li>
        </ul>
    </div>

    <div class="card">
        <h2>Revenue by Product</h2>
        <img src="visuals/revenue_by_product.png" alt="Revenue by Product Chart">
    </div>

    <div class="card">
        <h2>Revenue by Category</h2>
        <img src="visuals/revenue_by_category.png" alt="Revenue by Category Chart">
    </div>

    <div class="card">
        <h2>Revenue by City</h2>
        <img src="visuals/revenue_by_city.png" alt="Revenue by City Chart">
    </div>

</body>
</html> by City](visuals/revenue_by_city.png)