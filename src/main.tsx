import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'

import { loginUser } from './utils/firebase'

import './globals.css'

import LoginUser from './components/LoginUser'

createRoot(document.getElementById('root')!).render(
	<StrictMode>
		<LoginUser />
	</StrictMode>,
)
