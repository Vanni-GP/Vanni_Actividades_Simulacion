# simulacion_cola.py
import simpy
import random
import statistics

def cliente(env, nombre, servidor, mean_service, wait_times, service_times):
    llegada = env.now
    with servidor.request() as req:
        yield req
        espera = env.now - llegada
        wait_times.append(espera)
        servicio = random.expovariate(1.0 / mean_service)
        service_times.append(servicio)
        yield env.timeout(servicio)

def generador_llegadas(env, servidor, mean_interarrival, mean_service, num_clientes, wait_times, service_times):
    for i in range(num_clientes):
        inter = random.expovariate(1.0 / mean_interarrival)
        yield env.timeout(inter)
        env.process(cliente(env, f"Cliente {i+1}", servidor, mean_service, wait_times, service_times))

def correr_simulacion(mean_interarrival=5.0, mean_service=3.0, num_clientes=50, seed=42):
    random.seed(seed)
    env = simpy.Environment()
    servidor = simpy.Resource(env, capacity=1)
    wait_times = []
    service_times = []

    env.process(generador_llegadas(env, servidor, mean_interarrival, mean_service, num_clientes, wait_times, service_times))
    env.run()

    if wait_times:
        prom_espera = statistics.mean(wait_times)
        prom_serv = statistics.mean(service_times)
        prom_sistema = statistics.mean([w + s for w, s in zip(wait_times, service_times)])
        utilizacion = sum(service_times) / env.now
    else:
        prom_espera = prom_serv = prom_sistema = utilizacion = 0.0

    return {
        "clientes_simulados": len(wait_times),
        "tiempo_total_sim": env.now,
        "promedio_espera": prom_espera,
        "promedio_servicio": prom_serv,
        "promedio_en_sistema": prom_sistema,
        "utilizacion_servidor": utilizacion
    }

if __name__ == "__main__":
    resultados = correr_simulacion(mean_interarrival=5.0, mean_service=3.0, num_clientes=50)
    print("Resultados de la simulación (cola 1 cajero):")
    for k, v in resultados.items():
        if isinstance(v, float):
            print(f"{k}: {v:.3f}")
        else:
            print(f"{k}: {v}")
