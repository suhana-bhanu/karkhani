import React, { useState } from 'react';
import Plot from 'react-plotly.js';
import { Sliders } from 'lucide-react';

interface MobiusData {
  x: number[][];
  y: number[][];
  z: number[][];
}

function App() {
  const [radius, setRadius] = useState(3);
  const [width, setWidth] = useState(1);
  const [resolution, setResolution] = useState(100);
  const [data, setData] = useState<MobiusData | null>(null);

  const generateMobiusData = () => {
    const u = Array.from({ length: resolution }, (_, i) => (2 * Math.PI * i) / (resolution - 1));
    const v = Array.from({ length: resolution }, (_, i) => width * (i / (resolution - 1) - 0.5));
    
    const x: number[][] = [];
    const y: number[][] = [];
    const z: number[][] = [];

    for (let i = 0; i < resolution; i++) {
      x[i] = [];
      y[i] = [];
      z[i] = [];
      for (let j = 0; j < resolution; j++) {
        const uVal = u[j];
        const vVal = v[i];
        x[i][j] = (radius + vVal * Math.cos(uVal / 2)) * Math.cos(uVal);
        y[i][j] = (radius + vVal * Math.cos(uVal / 2)) * Math.sin(uVal);
        z[i][j] = vVal * Math.sin(uVal / 2);
      }
    }

    setData({ x, y, z });
  };

  React.useEffect(() => {
    generateMobiusData();
  }, [radius, width, resolution]);

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-6xl mx-auto">
        <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
          <div className="flex items-center gap-2 mb-6">
            <Sliders className="w-6 h-6 text-blue-600" />
            <h1 className="text-2xl font-bold text-gray-800">Mobius Strip Visualization</h1>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
            <div className="flex flex-col">
              <label className="text-sm font-medium text-gray-700 mb-1">Radius</label>
              <input
                type="range"
                min="1"
                max="5"
                step="0.1"
                value={radius}
                onChange={(e) => setRadius(Number(e.target.value))}
                className="w-full"
              />
              <span className="text-sm text-gray-600 mt-1">{radius}</span>
            </div>
            
            <div className="flex flex-col">
              <label className="text-sm font-medium text-gray-700 mb-1">Width</label>
              <input
                type="range"
                min="0.1"
                max="2"
                step="0.1"
                value={width}
                onChange={(e) => setWidth(Number(e.target.value))}
                className="w-full"
              />
              <span className="text-sm text-gray-600 mt-1">{width}</span>
            </div>
            
            <div className="flex flex-col">
              <label className="text-sm font-medium text-gray-700 mb-1">Resolution</label>
              <input
                type="range"
                min="20"
                max="150"
                step="5"
                value={resolution}
                onChange={(e) => setResolution(Number(e.target.value))}
                className="w-full"
              />
              <span className="text-sm text-gray-600 mt-1">{resolution}</span>
            </div>
          </div>

          {data && (
            <Plot
              data={[
                {
                  type: 'surface',
                  x: data.x,
                  y: data.y,
                  z: data.z,
                  colorscale: 'Viridis',
                  showscale: false,
                },
              ]}
              layout={{
                width: 800,
                height: 600,
                title: 'Mobius Strip',
                scene: {
                  camera: {
                    eye: { x: 1.5, y: 1.5, z: 1.5 },
                  },
                  aspectratio: { x: 1, y: 1, z: 1 },
                },
                margin: { t: 50, b: 0, l: 0, r: 0 },
              }}
              config={{ responsive: true }}
            />
          )}
        </div>
      </div>
    </div>
  );
}

export default App;