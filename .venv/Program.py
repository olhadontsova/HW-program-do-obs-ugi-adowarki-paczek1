print ("Hi!")
print ("This is program for packing parcels with weight restrictions, managing items, and calculating unused space.")
parcel_quantity = int(input("Enter the number of items to ship: "))
weights = []
for i in range(parcel_quantity):
    parcel_weight = float(input("Enter the weight of the product: "))
    if parcel_weight <1 or parcel_weight >10:
        print("Error. Not acceptable weigh of parcel. Should be from 1 to 10 kg.")
        continue
    weights.append(parcel_weight)
    print(f"All entered weights: {weights}")

    parcels = []
    current_parcel_weight = 0

for weight in weights:
    if current_parcel_weight + weight > 20:
        parcels.append(current_parcel_weight)
        current_parcel_weight = weight
    else:
        current_parcel_weight += weight
print (f"Tolal parcels: {len(parcels)}")
print (f"Total weight sent: {sum(parcels)} kg")
empty_space = len(parcels) * 20 - sum(parcels)
print(f"Total unused space: {empty_space} kg")
max_empty_space = max ([20 - parcel for parcel in parcels])
print (f"Pakage with the most unsudes spase {max_empty_space} kg")

