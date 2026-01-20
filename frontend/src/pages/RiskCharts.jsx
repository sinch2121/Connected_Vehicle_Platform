import {
  BarChart, Bar, XAxis, YAxis, Tooltip,
  ScatterChart, Scatter, CartesianGrid, Legend
} from "recharts";

export default function RiskCharts({ data }) {
  const categoryCount = data.reduce((acc, row) => {
    acc[row.risk_category] = (acc[row.risk_category] || 0) + 1;
    return acc;
  }, {});

  const barData = Object.keys(categoryCount).map((k) => ({
    category: k,
    count: categoryCount[k],
  }));

  return (
    <>
      <h3>Risk Distribution</h3>
      <BarChart width={500} height={300} data={barData}>
        <XAxis dataKey="category" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="count" fill="#8884d8" />
      </BarChart>

      <h3>Risk vs Anomaly</h3>
      <ScatterChart width={500} height={300}>
        <CartesianGrid />
        <XAxis dataKey="risk_score" name="Risk" />
        <YAxis dataKey="anomaly_score" name="Anomaly" />
        <Tooltip cursor={{ strokeDasharray: "3 3" }} />
        <Legend />
        <Scatter name="Vehicles" data={data} fill="#82ca9d" />
      </ScatterChart>
    </>
  );
}
