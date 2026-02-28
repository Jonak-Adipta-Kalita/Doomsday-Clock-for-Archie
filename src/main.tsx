import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'

import './globals.css'

import Clock from './components/Clock'

createRoot(document.getElementById('root')!).render(
	<StrictMode>
		<Clock />
	</StrictMode>,
)
