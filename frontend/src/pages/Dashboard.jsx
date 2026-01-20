import { useState } from "react";
import RiskCharts from "./RiskCharts";

import {
  ingestData,
  runFeatures,
  runProfiling,
  runRisk,
  trainML,
  scoreML,
  runFusion,
} from "../api/api";

export default function Dashboard() {
  const [file, setFile] = useState(null);
  const [log, setLog] = useState([]);
  const [fusedData, setFusedData] = useState([]);

  const addLog = (msg) => setLog((prev) => [...prev, msg]);

  /* =========================
     KPI CALCULATIONS
     ========================= */
  const totalVehicles = fusedData.length;

  const lowCount = fusedData.filter(v => v.risk_category === "LOW").length;
  const mediumCount = fusedData.filter(v => v.risk_category === "MEDIUM").length;
  const criticalCount = fusedData.filter(v => v.risk_category === "CRITICAL").length;

  const avgFusedRisk =
    fusedData.length > 0
      ? (
          fusedData.reduce((sum, v) => sum + v.fused_risk, 0) /
          fusedData.length
        ).toFixed(2)
      : 0;

  return (
    <div className="container">
      <h2>Connected Vehicle Risk Platform</h2>

      {/* Upload */}
      <div className="card">
        <h3>Upload Vehicle Data</h3>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <button
          onClick={async () => {
            await ingestData(file);
            addLog("Data ingested");
          }}
        >
          Upload
        </button>
      </div>

      {/* Pipeline */}
      <div className="card">
        <h3>Run Pipeline</h3>

        <button onClick={async () => { await runFeatures(); addLog("Features generated"); }}>
          Features
        </button>

        <button onClick={async () => { await runProfiling(); addLog("Profiling completed"); }}>
          Profiling
        </button>

        <button onClick={async () => { await runRisk(); addLog("Risk scored"); }}>
          Risk
        </button>

        <button onClick={async () => { await trainML(); addLog("ML trained"); }}>
          Train ML
        </button>

        <button onClick={async () => { await scoreML(); addLog("Anomalies scored"); }}>
          Score ML
        </button>

        <button
          onClick={async () => {
            const res = await runFusion();
            setFusedData(res.data.records);
            addLog("Fusion completed");
          }}
        >
          Fusion
        </button>
      </div>

      {/* KPI SUMMARY */}
      {/* KPI SUMMARY */}
{fusedData.length > 0 && (
  <div className="card">
    <h3>Risk Summary (KPI)</h3>

    <div className="kpi-grid">
      <div className="kpi-card kpi-neutral">
        Total<br />{totalVehicles}
      </div>

      <div className="kpi-card kpi-low">
        LOW<br />{lowCount}
      </div>

      <div className="kpi-card kpi-medium">
        MEDIUM<br />{mediumCount}
      </div>

      <div className="kpi-card kpi-critical">
        CRITICAL<br />{criticalCount}
      </div>

      <div className="kpi-card kpi-neutral">
        Avg Risk<br />{avgFusedRisk}
      </div>
    </div>
  </div>
)}

      {/* Status */}
      <div className="card">
        <h3>Status</h3>
        <ul className="status-list">
          {log.map((l, i) => (
            <li key={i}>{l}</li>
          ))}
        </ul>
      </div>

      {/* Fused Output Table */}
      {fusedData.length > 0 && (
        <div className="card">
          <h3>Fused Risk Output</h3>

          <table border="1" cellPadding="8">
            <thead>
              <tr>
                <th>Vehicle ID</th>
                <th>Risk Score</th>
                <th>Anomaly Score</th>
                <th>Fused Risk</th>
                <th>Category</th>
              </tr>
            </thead>
            <tbody>
              {fusedData.map((row, i) => (
                <tr key={i}
                className={row.risk_category === "CRITICAL" ? "critical-row" : ""}>
                  <td>{row.vehicle_id}</td>
                  <td>{row.risk_score.toFixed(2)}</td>
                  <td>{row.anomaly_score.toFixed(2)}</td>
                  <td>{row.fused_risk.toFixed(2)}</td>
                  <td>{row.risk_category}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Charts */}
      {fusedData.length > 0 && (
        <div className="card">
          <RiskCharts data={fusedData} />
        </div>
      )}
    </div>
  );
}
