X0 = 5
D = 5
DX = 1
N = 10
n = 200

function rho(x, y)
    exp(-((x-X0)^2 + y^2)/D^2) - exp(-((x+X0)^2 + y^2)/D^2)
end

function save_matrix(matrix, filename)
    open(filename, "w") do file
        for i=1:length(matrix)-1
            for j=1:length(matrix[i])-1
                write(file, string(matrix[i, j]))
                write(file, "\t")
                println(string(matrix[i, j]))
            end
            write(file, "\n")
        end
        
    end
end

function save_arr(arr, filename)
    open(filename, "w") do file
        for i=1:length(arr)
            write(file, string(arr[i]))
            write(file, "\t")
        end
        
    end
end

function get_a(grid_arr, rho_arr)
    output = 0
    for i = 2:2*N
        for j = 2:2*N
            part1 = (grid_arr[i+1, j] - grid_arr[i-1, j]) / (2*DX)
            part1 = 0.5*part1^2
            part2 = (grid_arr[i, j+1] - grid_arr[i, j-1]) / (2*DX)
            part2 = 0.5*part2^2
            part3 = -rho_arr[i, j] * grid_arr[i, j]
            output += part1 + part2 + part3
        end
    end
    return output * DX^2
end

function get_new_rho(grid_arr, i, j)
    - (grid_arr[i+1, j] + grid_arr[i-1, j] + grid_arr[i, j-1] + grid_arr[i, j+1] - 4 * grid_arr[i, j]) / DX^2
end

function fill_grid(grid_arr, rho_arr)
    for i = 2:2*N
        for j = 2:2*N
            grid_arr[i, j] = 0.25 * (grid_arr[i+1, j] + grid_arr[i-1, j] + grid_arr[i, j+1] + grid_arr[i, j-1] + rho_arr[i, j] * DX^2)
        end
    end
end

function main()
    rho_org = Array{Float64, 2}(undef, 2*N+1, 2*N+1)
    rho_new = Array{Float64, 2}(undef, 2*N+1, 2*N+1)
    grid = Array{Float64, 2}(undef, 2*N+1, 2*N+1)
    a = Array{Float64, 1}(undef, n)

    for i = 2:2*N
        for j = 2:2*N
            rho_org[i, j] = rho(i-N-1, j-N-1)
        end
    end

    for i = 1:n
        fill_grid(grid, rho_org)
        a[i] = get_a(grid, rho_org)
    end
    for i = 2:2*N
        for j = 2:2*N
            rho_new[i, j] = get_new_rho(grid, i, j)
        end
    end
    rho_diff = rho_new - rho_org

    x = 1:n
    println(rho_new)

    save_matrix(rho_diff, "rho_diff.txt")



end

main()
