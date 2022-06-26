const connectToDatabase = () => {
    const dummyPromise = new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log("dummyPromise")
            resolve();
        }, 1000)
    });
    return dummyPromise;
}

export default connectToDatabase;