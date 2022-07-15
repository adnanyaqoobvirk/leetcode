class ParkingSystem {
    int[] spaces;
    
    public ParkingSystem(int big, int medium, int small) {
        this.spaces = new int[]{0, big, medium, small};
    }
    
    public boolean addCar(int carType) {
        if(this.spaces[carType] > 0){
            this.spaces[carType]--;
            return true;
        } else
            return false;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */