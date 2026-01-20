import axios from "axios";

const API_BASE = "http://127.0.0.1:8000/api";

export const ingestData = (file) => {
  const formData = new FormData();
  formData.append("file", file);
  return axios.post(`${API_BASE}/ingest`, formData);
};

export const runFeatures = () => axios.post(`${API_BASE}/features/run`);
export const runProfiling = () => axios.post(`${API_BASE}/profile/run`);
export const runRisk = () => axios.post(`${API_BASE}/risk/run`);
export const trainML = () => axios.post(`${API_BASE}/ml/train`);
export const scoreML = () => axios.post(`${API_BASE}/ml/score`);
export const runFusion = () => axios.post(`${API_BASE}/fusion/run`);
