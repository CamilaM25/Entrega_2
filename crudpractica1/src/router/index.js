import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ListarView from '../views/ListarView.vue'
import CrearView from '../views/CrearView.vue'
import EditarView from '../views/EditarView.vue'
import PacienteView from '../views/PacienteView.vue'
import EspecialistaView from '../views/EspecialistaView.vue'
import ResultadosView from '../views/ResultadosView.vue'







const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/listar',
    name: 'listar',
    component: ListarView
  },
  {
    path: '/crear',
    name: 'crear',
    component: CrearView
  },
  {
    path: '/editar/:id',
    name: 'editar',
    component: EditarView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },

  {
    path: '/paciente',
    name: 'paciente',
    component: PacienteView
  },  
  {
    path: '/especialista',
    name: 'especialista',
    component: EspecialistaView
  },
  {
    path: '/resultados/:id',
    name: 'resultados',
    component: ResultadosView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
